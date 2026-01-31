import json
import logging
import re
import typing
from importlib.resources import files
from random import Random
from typing import List, Optional

from BaseClasses import Region, CollectionState, ItemClassification
from Options import OptionError
from . import data
from .logic.monster_logic import MonsterLogic
from .logic.quest_logic import QuestLogic
from .options.options import FarmType, StardewValleyOptions, IncludeEndgameLocations, ExcludeGingerIsland
from .regions.model import ConnectionData, RegionData, reverse_connection_name, RandomizationFlag
from .regions.vanilla_data import ginger_island_connections, vanilla_connections
from .stardew_rule import Received, StardewRule, True_, False_
from .strings.entrance_names import Entrance as StardewEntrance
from .strings.region_names import Region as StardewRegion
from .strings.tool_names import ToolMaterial

if typing.TYPE_CHECKING:
    from .regions import RegionFactory
    from . import StardewValleyWorld

directions = ["Left", "Up", "Right", "Down"]
direction_to_coord = {
    "Left": (-1, 0),
    "Up": (0, -1),
    "Right": (1, 0),
    "Down": (0, 1)
}

aliases = {
    StardewRegion.farm_house: "FarmHouse",
    StardewRegion.backwoods: StardewRegion.tunnel_entrance,
    StardewRegion.forest: "Cindersap Forest",
    StardewRegion.beach: "Pelican Beach",
    StardewRegion.town: "Pelican Town",
    StardewRegion.mountain: "Mountains",
    StardewRegion.desert: "Calico Desert",
    StardewRegion.hospital: "Harvey's Clinic",
    StardewRegion.harvey_room: "HarveyRoom",
    StardewRegion.alex_house: "Home of George, Evelyn & Alex",
    StardewRegion.trailer: "Home of Pam & Penny",
    StardewRegion.saloon: "Stardrop Saloon",
    StardewRegion.haley_house: "Home of Emily & Haley",
    StardewRegion.sam_house: "Home of Jodi, Kent & Sam",
    StardewRegion.purple_shorts_maze: "LewisBasement",
    StardewRegion.blacksmith: "Blacksmith",
    StardewRegion.museum: "Stardew Valley Museum & Library",
    StardewRegion.carpenter: "Carpenter's Shop",
    StardewRegion.sebastian_room: "SebastianRoom",
    StardewRegion.leo_treehouse: "LeoTreeHouse",
    StardewRegion.island_south: "IslandSouth",
    StardewRegion.island_east: "IslandEast",
    StardewRegion.island_south_east: "IslandSouthEast",
    StardewRegion.island_north: "IslandNorth",
    StardewRegion.field_office: "Island Field Office",
    StardewRegion.witch_swamp: "WitchSwamp",
    StardewRegion.witch_warp_cave: "WitchWarpCave",
    StardewRegion.witch_hut: "WitchHut",
    StardewRegion.mutant_bug_lair: "BugLand",
    StardewRegion.boat_tunnel: "BoatTunnel",
    StardewRegion.elliott_house: "Elliott's Cabin",
    StardewRegion.farm_cave: "FarmCave",
    StardewRegion.fish_shop: "Fish Shop",
    StardewRegion.mastery_cave: "MasteryCave",
    StardewRegion.oasis: "SandyHouse",
    StardewRegion.bus_tunnel: "Tunnel",
    StardewRegion.wizard_tower: "Wizard's Tower",
    StardewRegion.wizard_basement: "WizardBasement",
    StardewRegion.professor_snail_cave: "Island Mushroom Cave",
    StardewRegion.gourmand_frog_cave: "IslandFarmCave",
    StardewRegion.island_farmhouse: "IslandFarmHouse",
    StardewRegion.leo_hut: "IslandHut",
    StardewRegion.island_shrine: "IslandShrine",
    StardewRegion.pirate_cove: "IslandSouthEastCave",
    StardewRegion.island_west: "IslandWest"
}

for key in list(aliases.keys()):
    assert (aliases[key] != key)  # Remove the entry if this is ever triggered
    aliases[aliases[key]] = key

all_tiles = None


# TODO: Tile entrance to shipping
# TODO: Different sizes between tile locations and tile items
# TODO: Get items while exploring tiles to not always rely on bus stop


def alternate_name(region: str, option: "StardewValleyOptions"):
    if region in aliases:
        return aliases[region]

    farm_type = option.farm_type
    if farm_type == FarmType.option_standard:
        farm_name = "Standard Farm"
    elif farm_type == FarmType.option_riverland:
        farm_name = "Riverland Farm"
    elif farm_type == FarmType.option_forest:
        farm_name = "Forest Farm"
    elif farm_type == FarmType.option_hill_top:
        raise OptionError("Hilltop Farm is erroring")
        farm_name = "Hilltop Farm"
    # elif farm_type == FarmType.option_wilderness:
    #     farm_name = "Wilderness Farm"
    elif farm_type == FarmType.option_four_corners:
        farm_name = "Four Corners Farm"
    # elif farm_type == FarmType.option_beach:
    #     farm_name = "Beach Farm"
    elif farm_type == FarmType.option_meadowlands:
        farm_name = "Meadowlands Farm"
    else:
        # farm_name = "Farm Farm"
        raise OptionError("Farm type is not implemented")
    if region == "Farm":
        return farm_name
    elif region == farm_name:
        return "Farm"
    return region


def tilesanity_name_from_coord(region: str, x: int, y: int) -> str:
    return f"Tilesanity: {region} ({x}-{y})"


def tilesanity_coord_from_name(name: str) -> tuple[str, int, int]:
    pattern = r"Tilesanity: ([ \w'&,]+) +\((\d+)\-(\d+)\)"
    result = re.search(pattern, name)
    return result[1], int(result[2]), int(result[3])


def list_all_ap_ids() -> dict[str, int]:
    global all_tiles
    if all_tiles is not None:
        return all_tiles

    all_tiles = {}
    with files(data).joinpath("tiles.json").open() as file:
        tiles = json.load(file)
        current_id_base = 1_0000_0000_0000
        for area in tiles:
            used_coords = set()
            for coord in tiles[area]:
                coord = coord.split(", ")
                x = int(coord[0])
                y = int(coord[1])
                for i in range(1, 11):
                    x1 = x // i
                    y1 = y // i
                    if (x1, y1) not in used_coords:
                        tile_name = tilesanity_name_from_coord(area, x1, y1)
                        tile_id = current_id_base + x1 * 10000 + y1
                        all_tiles[tile_name] = tile_id
                        all_tiles[tile_name + " (lucky)"] = tile_id + current_id_base
                        used_coords.add((x1, y1))
            current_id_base += 1_0000_0000
    return all_tiles


def list_all_tiles(options: "StardewValleyOptions", maps_to_exclude: set[str]):
    all_tiles = set()
    with files(data).joinpath("tiles.json").open() as file:
        tiles = json.load(file)
        farm_name = alternate_name("Farm", options)

        for region in tiles:
            if region in maps_to_exclude:
                continue

            if region != "FarmHouse" and (not region.endswith("Farm") or region == farm_name):
                all_tiles.update([(region, coord) for coord in tiles[region]])

    return all_tiles


def connect(region1: Region, region2: Region, exit_name: str | None = None):
    region1.connect(region2, exit_name)


def er_connect(region1: Region, region2: Region, exit_name: str, regions_by_name: dict[str, Region], region_factory: "RegionFactory"):
    region1.create_exit(exit_name)
    buffer_region = region_factory(exit_name)
    regions_by_name[exit_name] = buffer_region
    buffer_region.create_er_target(reverse_connection_name(exit_name))
    connect(buffer_region, region2)


def create_regions_tilesanity(world: "StardewValleyWorld", region_factory: "RegionFactory",
                              region_data: dict[str, RegionData], player: int, random: Random, randomization_flag: RandomizationFlag):
    tile_coords = tuple[str, int, int]
    regions_by_name: dict[str, Region] = {}
    tiles_by_coords: dict[tile_coords, Region] = {}
    required_items: dict[tile_coords, List[str]] = {}
    connections = {connection.name: connection for connection in vanilla_connections} | {connection.name: connection for connection in
                                                                                         ginger_island_connections}
    entrances_coords_by_name: dict[str, tile_coords] = {}
    location_origin: dict[str, str] = {}
    entrance_points: dict[str, tuple[Optional[tile_coords], Optional[tile_coords]]]
    orphan_maps: list[tuple[str, str]] = []  # Starts as the list of all regions with an exists to then become the ones with no central point
    door_connections: dict[str, tuple[str, str]] = {}  # This is to delay connecting doors to tile since we have to go through orphans first
    banned_entrances: set[str] = {
        StardewEntrance.enter_quarry,
        StardewEntrance.enter_tide_pools,
        StardewEntrance.enter_lewis_bedroom,
        StardewEntrance.adventurer_guild_to_bedroom
    }
    banned_regions: set[str] = {
        StardewRegion.lewis_bedroom
    }

    maps_to_exclude = get_maps_to_exclude(world.options)

    all_tiles = list_all_tiles(world.options, maps_to_exclude)
    create_tiles_full(region_factory, regions_by_name, all_tiles, tiles_by_coords)

    # Get normal regions
    for region_name in region_data:
        if region_name in banned_regions:
            continue
        region: Region = region_factory(region_name)
        regions_by_name[region_name] = region

    # Add tiles connections between maps
    with files(data).joinpath("important_tiles.json").open() as file:
        important_tiles = json.load(file)
        farm_type = alternate_name("Farm", world.options)
        if farm_type in important_tiles:
            important_tiles["Farm"] = important_tiles[farm_type]

        for region in important_tiles:
            region: str
            if region == "Farm":
                real_region = farm_type
            elif region.endswith("Farm") or region in maps_to_exclude:
                continue
            else:
                real_region = region
            for tile in important_tiles[region]:
                pos = tile["Position"].split(", ")
                x = int(pos[0])
                y = int(pos[1])
                if len(tile["RequiredItems"]) > 0:
                    required_items[(real_region, x, y)] = tile["RequiredItems"]
                for entrance in tile["Entrances"]:
                    splited = entrance.split("!loc")
                    if len(splited) > 1:
                        location_origin[splited[0]] = tilesanity_name_from_coord(real_region, x, y)
                        continue

                    entrances_coords_by_name[entrance] = (real_region, x, y)

    for region_name in region_data:
        region: RegionData = region_data[region_name]
        for exit_name in region.exits:
            if exit_name in banned_entrances:
                continue
            connection: ConnectionData = connections[exit_name]
            connection_name = connection.name
            if connection_name in entrances_coords_by_name:
                r_name, x, y = entrances_coords_by_name.pop(connection_name)
                origin = tilesanity_name_from_coord(r_name, x, y)
            else:
                origin = region_name
            exit_connection_name = f"{connection_name}!exit"
            if exit_connection_name in entrances_coords_by_name:
                r_name, x, y = entrances_coords_by_name.pop(exit_connection_name)
                destination = tilesanity_name_from_coord(r_name, x, y)
                orphan_maps.append((connection_name, connection.destination))
            else:
                destination = connection.destination

            door_connections[connection_name] = (origin, destination)

    for entrance_name in entrances_coords_by_name:
        region, x, y = entrances_coords_by_name[entrance_name]
        if entrance_name.endswith("!exit"):
            continue
        elif entrance_name in region_data:
            destination = entrance_name
        else:
            region2, x2, y2 = entrances_coords_by_name[entrance_name]
            destination = tilesanity_name_from_coord(region2, x2, y2)
        origin = tilesanity_name_from_coord(region, x, y)
        if origin == destination:
            if __debug__:
                print(f"{entrance_name} unknown thus ignored")
            continue
        connect(regions_by_name[origin], regions_by_name[destination])
        i = 0
        while i < len(orphan_maps):
            if orphan_maps[i][1] == destination:
                del orphan_maps[i]
            else:
                i += 1

    for entrance_name, region_name in orphan_maps:
        origin, tile_destination = door_connections.pop(entrance_name)
        connection_data = connections[entrance_name]
        if connection_data.is_eligible_for_randomization(randomization_flag):
            er_connect(regions_by_name[origin], regions_by_name[region_name], entrance_name, regions_by_name, region_factory)
        else:
            connect(regions_by_name[origin], regions_by_name[region_name], entrance_name)
        connect(regions_by_name[region_name], regions_by_name[tile_destination], f"{region_name} to tile")

    for entrance_name, (origin, destination) in door_connections.items():
        connection_data = connections[entrance_name]
        if connection_data.is_eligible_for_randomization(randomization_flag):
            er_connect(regions_by_name[origin], regions_by_name[destination], entrance_name, regions_by_name, region_factory)
        else:
            connect(regions_by_name[origin], regions_by_name[destination], entrance_name)

    tile_size = world.options.tilesanity_size
    if tile_size > 1:
        for tile in tiles_by_coords:
            region: Region = tiles_by_coords[tile]
            parent: str = tile[0]
            x = tile[1]
            y = tile[2]
            big_region_name = tilesanity_name_from_coord(parent, int(x / tile_size), int(y / tile_size)) + " big"
            if big_region_name not in regions_by_name:
                big_region = region_factory(big_region_name)
                regions_by_name[big_region_name] = big_region
            connect(region, regions_by_name[big_region_name])

    # Then link tiles to one another
    for tile in tiles_by_coords:
        region: Region = tiles_by_coords[tile]
        parent: str = tile[0]
        x = tile[1]
        y = tile[2]
        for direction in directions:
            move = direction_to_coord[direction]
            ref = (parent, x + move[0], y + move[1])
            if ref in tiles_by_coords:
                linked_tile = tiles_by_coords[ref]
                connect(region, linked_tile)

    tile_to_coord = {}
    remaining_coords = set()
    for coord in tiles_by_coords:
        true_coord = (coord[0], coord[1] // tile_size, coord[2] // tile_size)
        tile_to_coord[tiles_by_coords[coord]] = true_coord
        remaining_coords.add(true_coord)
    world.tile_list = remaining_coords  # Just to be able to transmit how many tiles exist

    world.tilesanity_rulebuilder = lambda: define_tilesanity_item_rules(world, player, regions_by_name, tiles_by_coords, random, tile_to_coord,
                                                                        remaining_coords,
                                                                        required_items)
    world.location_origin_override = location_origin

    return regions_by_name


def get_maps_to_exclude(options: StardewValleyOptions):
    maps_to_exclude: set[str] = set()
    if options.include_endgame_locations == IncludeEndgameLocations.option_false:
        maps_to_exclude.add("Home of Pam & Penny")
    if options.exclude_ginger_island == ExcludeGingerIsland.option_true:
        maps_to_exclude |= {
            "IslandShrine",
            "IslandEast",
            "IslandWest",
            "IslandHut",
            "IslandFarmHouse",
            "Island Field Office",
            "IslandNorth",
            "IslandShrine",
            "IslandSouth",
            "IslandSouthEast",
            "IslandSouthEastCave",
            "LeoTreeHouse",
            "Colored Crystals Cave",
            "Qi's Walnut Room",
            "IslandFarmCave",
            "Shipwreck",
            "BoatTunnel",
            "Island Mushroom Cave"
        }
    return maps_to_exclude


def create_tiles_full(region_factory, regions_by_name, tiles, tiles_by_coords):
    for region, coords_name in tiles:
        coords = coords_name.split(", ")
        ref = (region, int(coords[0]), int(coords[1]))

        tile_name = tilesanity_name_from_coord(region, ref[1], ref[2])
        region = region_factory(tile_name)
        regions_by_name[tile_name] = region

        tiles_by_coords[ref] = region


logic_predicate_table = {
    "Dark Talisman": QuestLogic.has_dark_talisman,
    "Kill": MonsterLogic.can_kill_max,
    "Quest": QuestLogic.can_complete_quest,
    "Club Card": QuestLogic.has_club_card,
}


def requirement_rule(requirement: str, world: "StardewValleyWorld", player: int) -> StardewRule:
    # Or case
    splited = requirement.split(" OR ")
    if len(splited) != 1:
        rule_accumulator = False_()
        for i in range(len(splited)):
            rule_accumulator |= requirement_rule(splited[i], world, player)
        return rule_accumulator

    splited = requirement.split("!")
    # Special rules
    if splited[0] in logic_predicate_table:
        return logic_predicate_table[splited[0]](world.logic, *[arg for arg in splited[1:]])

    # Count items
    if len(splited) == 1:
        amount = 1
    else:
        splited[0] = "!".join(splited[:-1])
        # Reachability rules are denoted this way
        if splited[1] == "loc":
            return world.logic.region.can_reach_location(splited[0])
        if splited[1] == "reg":
            return world.logic.region.can_reach(splited[0])
        amount = int(splited[1])

    # Handle friendship
    splited = splited[0].split(" <3")
    if len(splited) > 1:
        return world.logic.relationship.has_hearts(splited[0], amount)

    # Handle tools
    splited = splited[0].split("$")
    if len(splited) > 1:
        return world.logic.tool.has_tool(splited[0], ToolMaterial.tiers[int(splited[1])])

    return Received(splited[0], player, amount)


def define_tilesanity_item_rules(world: "StardewValleyWorld", player: int, regions_by_name: dict[str, Region],
                                 tiles_by_coords: dict[tuple[str, int, int], Region],
                                 random: Random, tile_to_coord, remaining_coords, required_items):
    from worlds.stardew_valley.rules import StardewRuleCollector
    rule_collector = StardewRuleCollector(world.multiworld, world.player, world.content)
    for tile in required_items:
        requirements = required_items[tile]
        access_rule = True_()
        for requirement in requirements:
            access_rule &= requirement_rule(requirement, world, player)
        region = tiles_by_coords[tile]
        for entrance in region.entrances:
            rule_collector.set_entrance_rule(entrance.name, access_rule)

    tile_size = world.options.tilesanity_size
    world.tile_order = tile_order = []  # This list is sorted
    for tile in remaining_coords:
        x_min = tile[1] * tile_size
        y_min = tile[2] * tile_size
        x_max = x_min + tile_size
        y_max = y_min + tile_size
        tile_regions = set()
        for x in range(x_min, x_max):
            for y in range(y_min, y_max):
                coord = (tile[0], x, y)
                if coord in tiles_by_coords:
                    region = tiles_by_coords[coord]
                    tile_regions.add(region)

        tile_name = tilesanity_name_from_coord(tile[0], tile[1], tile[2])

        access_rule = Received(tile_name, player, 1)
        tile_order.append(tile_name)
        for region in tile_regions:
            for entrance in region.entrances:
                rule_collector.set_entrance_rule(entrance, access_rule)

    state = CollectionState(world.multiworld, allow_partial_entrances=True)
    state.sweep_for_advancements()
    world.tilesanity_rulebuilder = lambda: define_tilesanity_tile_rules(world, random, tile_to_coord,
                                                                        remaining_coords)


def define_tilesanity_tile_rules(world: "StardewValleyWorld", random: Random, tile_to_coord, remaining_coords):
    world.tile_order = tile_order = []  # This list is sorted

    state = CollectionState(world.multiworld, allow_partial_entrances=True)
    state.sweep_for_advancements()
    itempool = [item for item in world.multiworld.get_items() if item.player == world.player and item.name != "Progressive Tile" and item.advancement]
    from worlds.stardew_valley import StardewItem
    progressive_tile = StardewItem("Progressive Tile", ItemClassification.progression, None, world.player)
    random.shuffle(itempool)
    blocked_connections = sorted(state.blocked_connections[world.player], key=lambda entrance: entrance.name)
    random.shuffle(blocked_connections)
    item_score_per_tile = len(itempool) / len(remaining_coords) * 2
    item_score = -len(itempool) / 2
    logging.info(f"Ordering tilesanity tiles for {world.player_name} : {len(remaining_coords)} tiles left")
    for region in state.reachable_regions[1]:
        if region in tile_to_coord:
            coord = tile_to_coord[region]
            assert coord not in remaining_coords
    while len(remaining_coords) > 0:
        bias = random.betavariate(7, 1)
        i = int(bias * len(blocked_connections))
        if i >= len(blocked_connections):
            i = len(blocked_connections) - 1
            if i == -1:
                raise Exception(f"Failed at {len(remaining_coords)}")
            assert i != -1, f"No tile in {remaining_coords} is valid, no blocked connections"
        current_region = blocked_connections.pop(i).connected_region

        if current_region in tile_to_coord:
            coord = tile_to_coord[current_region]
            if coord in remaining_coords:
                remaining_coords.remove(coord)
                tile_order.append(tilesanity_name_from_coord(coord[0], coord[1], coord[2]))
                item_score += item_score_per_tile

                while item_score >= 1 and len(itempool) > 0:
                    state.collect(itempool.pop(), False)
                state.collect(progressive_tile, False)
                state.update_reachable_regions(world.player)
                for blocked_connection in state.blocked_connections[world.player]:
                    assert not blocked_connection.access_rule(state), f"{blocked_connection}: {blocked_connection.access_rule}"

                new_blocked_connections = sorted(state.blocked_connections[world.player].difference(blocked_connections), key=lambda entrance: entrance.name)
                random.shuffle(new_blocked_connections)
                blocked_connections += new_blocked_connections

                if len(remaining_coords) % 1000 == 0:
                    logging.info(f"Ordering tilesanity tiles for {world.player_name} : {len(remaining_coords)} tiles left")

    del world.tilesanity_rulebuilder


def get_neighbors(remaining_tiles, tile_region):
    neighbors = set()
    for region in tile_region:
        for entrance in region.exits:
            target: Region = entrance.connected_region
            if target.name.startswith("Tilesanity"):
                if target in remaining_tiles:
                    neighbors.add(target)
            else:
                return None  # Key tile
    return neighbors


def get_tile_regions(remaining_tiles, tile, tile_size, tiles_by_coords):
    x_min = tile[1] * tile_size
    y_min = tile[2] * tile_size
    x_max = x_min + tile_size
    y_max = y_min + tile_size
    tile_regions = [[]]
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            coord = (tile[0], x, y)
            if coord in tiles_by_coords:
                region = tiles_by_coords[(tile[0], x, y)]
                if region in remaining_tiles:
                    found_region = None
                    for i in range(len(tile_regions)):
                        tile_region = tile_regions[i]
                        if (len(tile_region) == 0
                                or ((tile[0], x - 1, y) in tiles_by_coords
                                    and tiles_by_coords[(tile[0], x - 1, y)] in tile_region)
                                or ((tile[0], x, y - 1) in tiles_by_coords
                                    and tiles_by_coords[(tile[0], x, y - 1)] in tile_region)):
                            tile_region.append(region)
                            if found_region is None:
                                found_region = tile_region
                            else:
                                found_region.extend(tile_region)
                                tile_regions.pop(i)
                                break
                    if found_region is None:
                        tile_regions.append([region])
    return tile_regions
