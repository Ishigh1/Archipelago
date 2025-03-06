import random

from BaseClasses import CollectionState
from worlds.stardew_valley import Tilesanity
from worlds.stardew_valley.options import SkillProgression, FarmType
from worlds.stardew_valley.strings.region_names import Region
from worlds.stardew_valley.test import setup_solo_multiworld

if __name__ == "__main__":
    world_options = {
        "tilesanity": Tilesanity.option_full,
        "tilesanity_size": 1,
        "tilesanity_simplification": 100,
        "farm_type": FarmType.option_standard,
        "skill_progression": SkillProgression.option_progressive
    }
    multiworld = setup_solo_multiworld(world_options)
    progitempool = []
    fake_items = multiworld.worlds[1].total_progression_items
    forced_items = []
    for item in multiworld.itempool:
        if item.advancement:
            progitempool.append(item)
    random.seed()
    random.shuffle(progitempool)
    state = CollectionState(multiworld)
    for item in progitempool:
        state.collect(item, True)
    state.prog_items[1]["fake_items"] = fake_items

    state.sweep_for_events()
    for region in multiworld.regions:
        if not state.can_reach_region(region.name, 1):
            print(region)