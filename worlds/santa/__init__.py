from typing import Dict, Any

from BaseClasses import Item, ItemClassification, Location, Region
from .Options import options
from ..AutoWorld import World


class SantaWorld(World):
    game = "Santa"
    topology_present = False
    item_name_to_id = {
        "Gift": 4573924180576428
    }
    location_name_to_id = {}
    for i in range(100):
        location_name_to_id["Happy Kid " + str(i + 1)] = 4573924180576428 + i
    option_definitions = options
    options: options

    def create_item(self, name: str) -> Item:
        if name == "Gift":
            return Item(name, ItemClassification.filler, 4573924180576428, self.player)
        raise KeyError(name)

    def get_filler_item_name(self) -> str:
        return "Gift"

    def create_location(self, name: str, kid_id: int, region):
        if name == "Happy Kid":
            return Location(self.player, name + " " + str(kid_id + 1), 4573924180576428 + kid_id, region)
        raise KeyError(name)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for i in range(self.options.locations.value):
            menu.locations.append(self.create_location("Happy Kid", i + 1, menu))

    def create_items(self) -> None:
        for _ in range(self.options.locations.value):
            self.multiworld.itempool.append(self.create_item("Gift"))

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: True

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "locations": self.options.locations.value
        }