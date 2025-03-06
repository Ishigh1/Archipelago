import logging
import random

from BaseClasses import CollectionState
from worlds.stardew_valley.options import *
from worlds.stardew_valley.strings.goal_names import Goal as GoalName
from worlds.stardew_valley.test import setup_solo_multiworld

if __name__ == "__main__":
    spot_name = "Spouse Stardrop"


    def can_reach(state: CollectionState) -> bool:
        return state.can_reach_location(spot_name, 1)


    world_options = {
        "goal": Goal.option_full_shipment,
        "tilesanity": Tilesanity.option_nope,
        "tilesanity_size": 5,
        "museumsanity": Museumsanity.option_all,
        "elevator_progression": ElevatorProgression.option_progressive_from_previous_floor,
        "friendsanity": Friendsanity.option_all,
        FriendsanityHeartSize.internal_name: 1,
        "farm_type": FarmType.option_standard,
        "cropsanity": Cropsanity.option_enabled,
        "fishsanity": Fishsanity.option_all,
        "shipsanity": Shipsanity.option_everything,
        "craftsanity": Craftsanity.option_all,
        "chefsanity": Chefsanity.option_all,
        "quest_locations": QuestLocations.default,
        "mods": [],
        "start_inventory": {}
    }
    multiworld = setup_solo_multiworld(world_options)
    progitempool = multiworld.precollected_items[1]
    multiworld.precollected_items.clear()
    world = multiworld.worlds[1]
    fake_items = world.total_progression_items
    for item in multiworld.itempool:
        if item.advancement:
            if item.name == "Progressive Tile" and len(world.tile_list) > 0:
                item.name = world.tile_list.pop()
                item.code = world.item_name_to_id[item.name]
            progitempool.append(item)

    for entrance in multiworld.get_entrances(1):
        access_rule = entrance.access_rule
        if hasattr(access_rule, 'switch_rule'):
            access_rule.switch_rule(True)

    state = CollectionState(multiworld)
    true_items = []
    for item in progitempool:
        state.collect(item, True)
        true_items.append(item.name)
    state.prog_items[1]["fake_items"] = fake_items
    state.sweep_for_events()
    assert can_reach(state)

    random.seed()
    random.shuffle(progitempool)
    min_items = None
    while True:
        progitempool_copy = progitempool.copy()
        forced_items = []
        while len(progitempool_copy) > 0:
            prog_item = progitempool_copy.pop()
            state = CollectionState(multiworld)
            for item in (progitempool_copy + forced_items):
                state.collect(item, True)
            state.prog_items[1]["fake_items"] = fake_items
            state.sweep_for_events()
            if not can_reach(state):
                forced_items.append(prog_item)
        if min_items is None or len(min_items) > len(forced_items):
            attempt = 0
            min_items = forced_items
        for item in forced_items:
            progitempool.remove(item)
            progitempool.append(item)
        break

    while fake_items > -1:
        state = CollectionState(multiworld)
        for item in min_items:
            state.collect(item, True)
        state.prog_items[1]["fake_items"] = fake_items
        state.sweep_for_events()
        if not can_reach(state):
            break
        fake_items -= 1
    fake_items += 1

    state = CollectionState(multiworld)
    true_items = []
    for item in min_items:
        state.collect(item, True)
        true_items.append(item.name)
    state.prog_items[1]["fake_items"] = fake_items
    state.sweep_for_events()
    assert can_reach(state)

    events = []
    item_count = 0
    for item in state.prog_items[1]:
        count = state.prog_items[1][item]
        item_count += count
        events.append((item, count))
    print(f"Progression needed = {item_count * 100 / multiworld.worlds[1].total_progression_items}% ({fake_items} extras)")
    events.sort()
    for item, count in events:
        if item in true_items:
            if count == 1:
                print(item + " (item)")
            else:
                print(f"{item} * {count} (item)")
    for item, count in events:
        if item not in true_items:
            print(item + " (event)")

    reachable_regions = state.reachable_regions[1]

    print(f"Currently reachable regions : {sorted(reachable_regions, key=(lambda r: r.name))}")

    reachable_location = [location for location in multiworld.get_locations(1) if state.can_reach_location(location.name, 1) and location.address]
    print(f"{len(reachable_location)} currently reachable locations : {sorted(reachable_location, key=(lambda l: l.name))}")
