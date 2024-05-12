import logging
import re
from random import Random
from typing import Dict, Tuple, List, Optional, Set

from BaseClasses import Entrance, Region
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


# The random path find was inspired by chiseled-random-paths from BorisTheBrave
def create_grid(point: Tuple[str, int, int], options: StardewValleyOptions, all_tiles) -> Tuple[Set[Tuple[int, int]], Dict[Tuple[int, int], str], str]:
    region = point[0]
    tiles = []
    region_names = [region]
    tile_to_name = {}

    region_names.append(alternate_name(region, options))
    for location in all_tiles:
        if location.region in region_names:
            pattern = r'\b\d+\b'
            coords = re.findall(pattern, location.name)
            tile = (int(coords[0]), int(coords[1]))
            tiles.append(tile)
            tile_to_name[tile] = location.name

    point = (point[1], point[2])
    tiles.remove(point)
    grid = set()
    stack = [point]
    grid.add(point)

    while len(stack) > 0:
        point = stack.pop()
        for direction in directions:
            move = direction_to_coord[direction]
            new_point = (point[0] + move[0], point[1] + move[1])
            if new_point in tiles:
                tiles.remove(new_point)
                grid.add(new_point)
                stack.append(new_point)

    region_name = region
    if tile_to_name[point] != tilesanity_name_from_coord(region_name, point[0], point[1]):
        region_name = alternate_name(region_name, options)
    return grid, tile_to_name, region_name


def find_path(grid: Set[Tuple[int, int]], locked_points: List[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
    path = [locked_points[0]]
    if len(locked_points) == 1:
        return path
    weight_map = {locked_points[0]: 0}
    current_weights = [locked_points[0]]
    next_weights = []
    next_weight = 1
    while len(current_weights) != 0:
        for point in current_weights:
            for direction in directions:
                move = direction_to_coord[direction]
                new_point = (point[0] + move[0], point[1] + move[1])
                if new_point in grid and new_point not in weight_map:
                    weight_map[new_point] = next_weight
                    next_weights.append(new_point)
        for locked_point in locked_points:
            if locked_point not in weight_map:
                break
        else:
            break

        current_weights = next_weights
        next_weights = []
        next_weight += 1
    else:
        return None

    for locked_point in locked_points:
        while weight_map[locked_point] != 0:
            if locked_point not in path:
                path.append(locked_point)
            current_weight = weight_map[locked_point]
            for direction in directions:
                move = direction_to_coord[direction]
                new_point = (locked_point[0] + move[0], locked_point[1] + move[1])
                if new_point in weight_map:
                    if weight_map[new_point] < current_weight:
                        locked_point = new_point
                        break
    return path


def get_tiles_for_region(world: "StardewValleyWorld", entry_points: List[Tuple[str, int, int]], random: Random, options: StardewValleyOptions, all_tiles) \
        -> Tuple[List[Tuple[int, int]], Dict[Tuple[int, int], str]]:
    region = entry_points[0]
    grid, tiles_to_name, region_name = create_grid(region, world.options, all_tiles)
    logging.info(f"Selecting tiles for {region_name}")
    all_keys = []
    tile_size = options.tilesanity_size
    for (x, y) in grid:
        key = (int(x / tile_size), int(y / tile_size))
        if key not in all_keys:
            all_keys.append(key)
    keys_left = all_keys.copy()
    starting_keys = len(all_keys)
    objective = starting_keys * options.tilesanity_simplification / 100
    locked_points = []
    for entry_point in entry_points:
        locked_point = (entry_point[1], entry_point[2])
        locked_points.append(locked_point)
        locked_key = (locked_point[0] // tile_size, locked_point[1] // tile_size)
        if locked_key in keys_left:
            keys_left.remove(locked_key)

    path = find_path(grid, locked_points)
    random.shuffle(keys_left)
    progress = starting_keys
    iteration = 0
    while len(keys_left) > objective:
        iteration += 1
        current_point = keys_left.pop()
        old_grid = grid.copy()
        first_x = current_point[0] * tile_size
        first_y = current_point[1] * tile_size
        disturbed_path = False
        for x in range(first_x, first_x + tile_size):
            for y in range(first_y, first_y + tile_size):
                point = (x, y)
                if point in grid:
                    grid.remove(point)
                    if point in path:
                        disturbed_path = True
        if disturbed_path:
            new_path = find_path(grid, locked_points)
            if new_path is None:
                grid = old_grid
                continue
            else:
                path = new_path
                world.excluded_tiles.append(tilesanity_name_from_coord(region_name, current_point[0], current_point[1]))
        else:
            world.excluded_tiles.append(tilesanity_name_from_coord(region_name, current_point[0], current_point[1]))
        if progress - len(keys_left) >= 500:
            progress = len(keys_left)
            logging.info(f"Selecting tiles for {region_name} ({starting_keys - progress} / {starting_keys - objective})")
        if iteration == 50:
            iteration = 0
            simplify_grid(grid, locked_points, keys_left, tile_size)

    if len(keys_left) > 0:
        simplify_grid(grid, locked_points, keys_left, tile_size)

    return list(grid), tiles_to_name


def simplify_grid(grid, locked_points, keys_left, tile_size):
    point = (locked_points[0][0], locked_points[0][1])
    stack = [point]
    i = 0
    while len(stack) > i:
        point = stack[i]
        for direction in directions:
            move = direction_to_coord[direction]
            new_point = (point[0] + move[0], point[1] + move[1])
            if new_point in grid and new_point not in stack:
                stack.append(new_point)
        i += 1

    for point in grid.copy():
        if point not in stack:
            grid.remove(point)

    new_keys_left = []
    for key in keys_left:
        x_min = key[0] * tile_size
        y_min = key[1] * tile_size
        for x in range(x_min, x_min + tile_size):
            for y in range(y_min, y_min + tile_size):
                if (x, y) in grid:
                    break
            else:
                continue
            break
        else:
            continue
        new_keys_left.append(key)
    return new_keys_left


def select_tiles(world, entry_points: Dict[Tuple[str, int, int], List[ConnectionData]], random: Random, options: StardewValleyOptions, all_tiles) \
        -> Tuple[Dict[str, List[Tuple[int, int]]], Dict[str, Dict[Tuple[int, int], str]]]:
    tiles = {}
    names = {}
    for entry_point in entry_points:
        if entry_point[0] not in tiles:
            current_region = entry_point[0]
            region_entry_points = []
            for entry_point2 in entry_points:
                if entry_point2[0] == current_region:
                    region_entry_points.append(entry_point2)

            tiles[current_region], names[current_region] = get_tiles_for_region(world, region_entry_points, random, options, all_tiles)

    return tiles, names


def list_all_tiles(options):
    all_tiles = set()
    farm_name = alternate_name("Farm", options)

    for location_data in locations_by_tag[LocationTags.TILESANITY]:
        if LocationTags.NOT_TILE not in location_data.tags and location_data.region != "FarmHouse" and \
                (not location_data.region.endswith("Farm") or location_data.region == farm_name):
            all_tiles.add(location_data)

    return all_tiles


def create_regions_tilesanity(world, region_factory: RegionFactory, region_data: Dict[str, RegionData],
                              options: StardewValleyOptions, player: int, random: Random):
    regions_by_name: Dict[str: Region] = {}
    entrances_by_name: Dict[str: Entrance] = {}
    tiles_by_coords: Dict[Tuple[str, int, int]: Region] = {}
    entry_points: Dict[Tuple[str, int, int]: List[ConnectionData]] = {}
    normal_connections: Dict[str: ConnectionData] = {}

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

    world.excluded_tiles = []
    all_tiles = list_all_tiles(options)
    if options.tilesanity_simplification == 100:
        create_tiles_full(entrances_by_name, region_factory, regions_by_name, all_tiles, tiles_by_coords)
    else:
        tiles, names = select_tiles(world, entry_points, random, options, all_tiles)
        create_tiles_simplified(entrances_by_name, region_factory, regions_by_name, tiles, names, tiles_by_coords)

    tile_size = options.tilesanity_size
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
                if tile_size == 1:
                    item_name = linked_tile.name
                else:
                    (region_name, _, _) = tilesanity_coord_from_name(linked_tile.name)
                    item_name = tilesanity_name_from_coord(region_name, int(ref[1] / tile_size), int(ref[2] / tile_size))

                entrance = region.connect(linked_tile, rule=lambda state, name=item_name: state.has(name, player))
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
            if tile_size == 1:
                item_name = destination.name
            else:
                (region_name, _, _) = tilesanity_coord_from_name(destination.name)
                item_name = tilesanity_name_from_coord(region_name, int(x / tile_size), int(y / tile_size))
            entrance.access_rule = lambda state, name=item_name: state.has(name, player)

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
                if tile_size == 1:
                    item_name = destination.name
                else:
                    (region_name, _, _) = tilesanity_coord_from_name(destination.name)
                    item_name = tilesanity_name_from_coord(region_name, int(x / tile_size), int(y / tile_size))
                entrance = origin.connect(destination, data.name, lambda state, name=item_name: state.has(name, player))
                entrances_by_name[entrance.name] = entrance

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


def create_tiles_simplified(entrances_by_name, region_factory, regions_by_name, tiles, names, tiles_by_coords):
    for region_name in tiles:
        for tile in tiles[region_name]:
            x = tile[0]
            y = tile[1]
            name = names[region_name][(x, y)]
            ref = (region_name, x, y)

            region: Region = region_factory(name, [])
            regions_by_name[name] = region

            tiles_by_coords[ref] = region
            for entrance in region.exits:
                entrances_by_name[entrance.name] = entrance
