from functools import reduce
from typing import Dict, Any

from BaseClasses import ItemClassification, Region, Entrance
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from .Items import *
from .Locations import *
from .Logic import *
from .Options import itb_options
from .Squads import *


class IntoTheBreachWorld(World):
    """A strategy turn based game"""
    game = "Into the Breach"
    option_definitions = itb_options
    topology_present = True

    base_id = 6777699702823011  # thanks random.org

    item_name_to_id = {name: id for
                       id, name in enumerate(itb_items, base_id)}
    locations = reduce(lambda x, y: x + y, itb_locations.values(), [])
    location_name_to_id = {name: id for
                           id, name in enumerate(locations, base_id)}

    item_name_groups = {
    }

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.randomized_squads = None

    def generate_early(self):
        if self.multiworld.randomize_squads[self.player]:
            self.randomized_squads = shuffle_teams(self.multiworld.random)

    def create_item(self, item: str):
        if item == "Unlock Hive":
            classification = ItemClassification.progression_skip_balancing
        elif item in itb_progression_items:
            classification = ItemClassification.progression
        elif item in itb_trap_items:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        return MyGameItem(item, classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str):
        return MyGameItem(event, True, None, self.player)

    def create_location(self, name, region):
        return MyGameLocation(self.player, name, self.location_name_to_id[name], region)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for squad_name in itb_locations:
            squad_region = Region(squad_name + " Squad", self.player, self.multiworld)
            squad_region.locations = [self.create_location(achievement, squad_region) for achievement in
                                      itb_locations[squad_name]]

            entrance = Entrance(self.player, "Use squad " + squad_name, menu)
            if squad_name != "Rift Walkers":
                set_rule(entrance, lambda state, squad=squad_name: state.has("Unlock " + squad, self.player))
            menu.exits.append(entrance)
            entrance.connect(squad_region)

            self.multiworld.regions.append(squad_region)

    def create_items(self) -> None:
        item_count = 0
        for item in itb_progression_items:
            if item == "3 Starting Grid Defense":
                count = 5
            elif item == "2 Starting Grid Power":
                count = 2
            else:
                count = 1

            item_count += count
            for i in range(count):
                self.multiworld.itempool.append(self.create_item(item))

        locations_count = len([location
                               for location in self.multiworld.get_locations(self.player)
                               if not location.event])

        random = self.multiworld.random
        while locations_count > item_count:
            if random.randint(1, 3) == 1:
                item = random.choice(itb_trap_items)
            else:
                item = random.choice(itb_filler_items)

            self.multiworld.itempool.append(self.create_item(item))
            item_count += 1

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.can_beat_the_game(self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.randomized_squads
