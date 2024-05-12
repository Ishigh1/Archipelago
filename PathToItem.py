import random

from BaseClasses import CollectionState
from worlds.stardew_valley.options import *
from worlds.stardew_valley.test import setup_solo_multiworld


if __name__ == "__main__":
    spot_name = "Craft Slime Egg-Press"
    world_options = {
        "tilesanity": Tilesanity.option_nope,
        "farm_type": FarmType.option_riverland,
        "shipsanity": Shipsanity.option_everything,
        "craftsanity": Craftsanity.option_all,
    }
    multiworld = setup_solo_multiworld(world_options)
    progitempool = []
    fake_items = multiworld.worlds[1].total_progression_items
    for item in multiworld.itempool:
        if item.advancement:
            progitempool.append(item)
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
            if not state.can_reach_location(spot_name, 1):
                forced_items.append(prog_item)
        if min_items is None or len(min_items) > len(forced_items):
            attempt = 0
            min_items = forced_items
        for item in forced_items:
            progitempool.remove(item)
            progitempool.append(item)
        else:
            attempt += 1
            if attempt == 50:
                break
            if attempt % 10 == 0:
                random.shuffle(progitempool)

    while fake_items > -1:
        state = CollectionState(multiworld)
        for item in min_items:
            state.collect(item, True)
        state.prog_items[1]["fake_items"] = fake_items
        state.sweep_for_events()
        if not state.can_reach_location(spot_name, 1):
            break
        fake_items -= 1
    fake_items += 1

    state = CollectionState(multiworld)
    for item in min_items:
        state.collect(item, True)
    state.prog_items[1]["fake_items"] = fake_items
    state.sweep_for_events()
    assert state.can_reach_location(spot_name, 1)

    min_items.sort()
    for item in min_items:
        print(item)

    item_count = 0
    for item in state.prog_items[1]:
        item_count += state.prog_items[1][item]
    print(f"Progression needed = {item_count * 100 / multiworld.worlds[1].total_progression_items}%")