import logging
import re
from collections import deque
from random import Random
from typing import Tuple, List, Hashable, Callable

from BaseClasses import Entrance, Region, CollectionState
from worlds.stardew_valley.locations import LocationTags, locations_by_tag
from worlds.stardew_valley.options import FarmType, StardewValleyOptions
from worlds.stardew_valley.region_classes import ConnectionData, RegionData
from worlds.stardew_valley.regions import RegionFactory, vanilla_connections, vanilla_regions
from worlds.stardew_valley.strings.region_names import Region as StardewRegion

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
    StardewRegion.desert: "Calico Desert"
}

for key in list(aliases.keys()):
    assert (aliases[key] != key)  # Remove the entry if this is ever triggered
    aliases[aliases[key]] = key


def alternate_name(region: str, option: StardewValleyOptions):
    if region in aliases:
        return aliases[region]

    farm_type = option.farm_type
    if farm_type == FarmType.option_standard:
        farm_name = "Standard Farm"
    elif farm_type == FarmType.option_riverland:
        farm_name = "Riverland Farm"
    else:
        raise NotImplemented("Farm type is not implemented")
    if region == "Farm":
        return farm_name
    elif region == farm_name:
        return "Farm"
    return region


def tilesanity_name_from_coord(region: str, x: int, y: int):
    return f"Tilesanity: {region} ({x}-{y})"


def tilesanity_coord_from_name(name: str):
    pattern = r'Tilesanity: ([ \w]+) +\((\d+)\-(\d+)\)'
    result = re.search(pattern, name)
    return result[1], int(result[2]), int(result[3])


def list_all_tiles(options):
    all_tiles = set()
    farm_name = alternate_name("Farm", options)

    for location_data in locations_by_tag[LocationTags.TILESANITY]:
        if LocationTags.NOT_TILE not in location_data.tags and location_data.region != "FarmHouse" and \
                (not location_data.region.endswith("Farm") or location_data.region == farm_name):
            all_tiles.add(location_data)

    return all_tiles


def create_regions_tilesanity(world: "StardewValleyWorld", region_factory: RegionFactory,
                              region_data: dict[str, RegionData], player: int, random: Random):
    regions_by_name: dict[str, Region] = {}
    entrances_by_name: dict[str, Entrance] = {}
    tiles_by_coords: dict[tuple[str, int, int], Region] = {}
    entry_points: dict[Tuple[str, int, int], List[ConnectionData]] = {}
    normal_connections: dict[str, ConnectionData] = {}

    connections = {connection.name: connection for connection in vanilla_connections}
    all_connections: List[ConnectionData] = []
    for region_name in region_data:
        region = region_data[region_name]
        for exit_name in region.exits:
            connection: ConnectionData = connections[exit_name]
            connection = ConnectionData(connection.name, connection.destination, region_name, entry_coord=connection.entry_coord,
                                        exit_coord=connection.exit_coord, flag=connection.flag)
            all_connections.append(connection)

    # Find exit tiles
    for vanilla_connection in all_connections:
        if vanilla_connection.entry_coord:
            ref = (vanilla_connection.origin, vanilla_connection.entry_coord[0],
                   vanilla_connection.entry_coord[1])
            if ref in entry_points:
                entry_points[ref].append(vanilla_connection)
            else:
                entry_points[ref] = [vanilla_connection]
        else:
            normal_connections[vanilla_connection.name] = vanilla_connection
        if vanilla_connection.exit_coord:
            ref = (vanilla_connection.destination, vanilla_connection.exit_coord[0],
                   vanilla_connection.exit_coord[1])
            connection = ConnectionData(vanilla_connection.reverse,
                                        vanilla_connection.origin,
                                        vanilla_connection.destination,
                                        entry_coord=vanilla_connection.exit_coord,
                                        exit_coord=vanilla_connection.entry_coord)
            if ref in entry_points:
                entry_points[ref].append(connection)
            else:
                entry_points[ref] = [connection]

    # Add vanilla connection tiles
    for data in vanilla_regions:
        if data.main_point:
            ref = (data.name, data.main_point[0], data.main_point[1])
            connection_data = ConnectionData(data.name, data.name, data.name, entry_coord=data.main_point)
            if ref in entry_points:
                entry_points[ref].append(connection_data)
            else:
                entry_points[ref] = [connection_data]

    all_tiles = list_all_tiles(world.options)
    create_tiles_full(entrances_by_name, region_factory, regions_by_name, all_tiles, tiles_by_coords)

    tile_size = world.options.tilesanity_size
    if tile_size > 1:
        for tile in tiles_by_coords:
            region: Region = tiles_by_coords[tile]
            parent: str = tile[0]
            x = tile[1]
            y = tile[2]
            big_region_name = tilesanity_name_from_coord(parent, int(x / tile_size), int(y / tile_size)) + " big"
            if big_region_name not in regions_by_name:
                big_region = region_factory(big_region_name, [])
                regions_by_name[big_region_name] = big_region
            entrance = region.connect(regions_by_name[big_region_name])
            entrances_by_name[entrance.name] = entrance

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
                entrance = region.connect(linked_tile)
                entrances_by_name[entrance.name] = entrance

    # Get normal regions
    for region_name in region_data:
        data = region_data[region_name]
        region = region_factory(region_name, [exit_name for exit_name in data.exits if exit_name in normal_connections])

        for entrance in region.exits:
            entrances_by_name[entrance.name] = entrance

        regions_by_name[region_name] = region

    # Put down normal connections
    for connection_name in normal_connections:
        entrance = entrances_by_name[connection_name]
        data = normal_connections[connection_name]
        if data.exit_coord is None:
            entrance.connect(regions_by_name[data.destination])
        else:
            x = data.exit_coord[0]
            y = data.exit_coord[1]
            if (data.destination, x, y) in tiles_by_coords:
                origin_region = data.destination
            else:
                origin_region = alternate_name(data.destination, world.options)
            destination = tiles_by_coords[(origin_region, x, y)]
            entrance.connect(destination)

    # Put down tile connections
    for connection_point in entry_points:
        for data in entry_points[connection_point]:
            x = data.entry_coord[0]
            y = data.entry_coord[1]
            if (data.origin, x, y) in tiles_by_coords:
                origin_region = data.origin
            else:
                origin_region = alternate_name(data.origin, world.options)
            origin: Region = tiles_by_coords[(origin_region, x, y)]
            if data.exit_coord is None:
                entrance = origin.connect(regions_by_name[data.destination], data.name)
                entrances_by_name[entrance.name] = entrance
            else:
                x = data.exit_coord[0]
                y = data.exit_coord[1]
                if (data.destination, x, y) in tiles_by_coords:
                    target_region = data.destination
                else:
                    target_region = alternate_name(data.destination, world.options)
                destination = tiles_by_coords[(target_region, x, y)]
                entrance = origin.connect(destination, data.name)
                entrances_by_name[entrance.name] = entrance

    define_tilesanity_rules(world, player, regions_by_name, entrances_by_name, tiles_by_coords, random)

    return regions_by_name, entrances_by_name


def create_tiles_full(entrances_by_name, region_factory, regions_by_name, tiles, tiles_by_coords):
    for location in tiles:
        name = location.name
        pattern = r'\b\d+\b'
        coords = re.findall(pattern, name)
        ref = (location.region, int(coords[0]), int(coords[1]))

        region = region_factory(name, [])
        regions_by_name[name] = region

        tiles_by_coords[ref] = region
        for entrance in region.exits:
            entrances_by_name[entrance.name] = entrance


def is_component(first_region: Region, other_tiles: set[Region], excluded_tiles_set: set[Region]) -> bool:
    explored_tiles = set()
    region_queue = deque()
    region_queue.append(first_region)
    while region_queue:
        region = region_queue.popleft()
        for entrance in region.exits:
            target = entrance.connected_region
            if target not in excluded_tiles_set and target not in explored_tiles:
                other_tiles.discard(target)
                if not other_tiles:
                    return True
                region_queue.append(target)
                explored_tiles.add(target)
    return False


def define_tilesanity_rules(world: "StardewValleyWorld", player: int, regions_by_name: dict[str, Region],
                            entrances_by_name: dict[str, Entrance], tiles_by_coords: dict[tuple[str, int, int], Region],
                            random: Random):
    menu = regions_by_name["Menu"]
    tile_order = []  # This list is sorted
    tile_size = world.options.tilesanity_size

    tile_to_coord = {}
    remaining_coords = set()
    for coord in tiles_by_coords:
        true_coord = (coord[0], coord[1] // tile_size, coord[2] // tile_size)
        tile_to_coord[tiles_by_coords[coord]] = true_coord
        remaining_coords.add(true_coord)

    queue = [menu]
    explored_regions = set(queue)
    while len(remaining_coords) > 0:
        current_region = queue.pop(random.randrange(0, len(queue)))
        if current_region in tile_to_coord:
            coord = tile_to_coord[current_region]
            if coord in remaining_coords:
                remaining_coords.remove(coord)
                tile_order.append(coord)
        for entrance in current_region.exits:
            exit_region = entrance.connected_region
            if exit_region not in explored_regions:
                explored_regions.add(exit_region)
                queue.append(exit_region)

    from worlds.stardew_valley.stardew_rule import CombinableStardewRule, StardewRule

    class TilesanityRule(CombinableStardewRule):
        player: int
        tile_name: str
        tile_count: int
        access_rule: Callable[[CollectionState], bool]
        specific_rule: bool

        def __init__(self, player: int, tile_name: str, tile_count: int):
            self.player = player
            self.tile_name = tile_name
            self.tile_count = tile_count
            self.access_rule = lambda state: state.has("Progressive Tile", self.player, self.tile_count)
            self.specific_rule = False

        @property
        def combination_key(self) -> Hashable:
            return "Progressive Tile"

        @property
        def value(self) -> int:
            return self.tile_count

        def __call__(self, state: CollectionState) -> bool:
            return self.access_rule(state)

        def evaluate_while_simplifying(self, state: CollectionState) -> Tuple[StardewRule, bool]:
            return self, self(state)

        def __repr__(self) -> str:
            if self.specific_rule:
                return f"Received {self.tile_name} ({self.tile_count} Progressive Tile)"
            else:
                return f"Received {self.tile_count} Progressive Tile ({self.tile_name})"

        def switch_rule(self, specific: bool) -> None:
            self.specific_rule = specific
            if specific:
                self.access_rule = lambda state: state.has(self.tile_name, self.player)
            else:
                self.access_rule = lambda state: state.has("Progressive Tile", self.player, self.tile_count)

    tile_names = []
    for i in range(len(tile_order)):
        tile = tile_order[i]
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
        tile_names.append(tile_name)

        access_rule = TilesanityRule(player, tile_name, i + 1)

        for region in tile_regions:
            for entrance in region.entrances:
                entrance.access_rule = access_rule

    world.tile_list = tile_names


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
