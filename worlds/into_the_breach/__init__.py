from typing import TextIO, Optional

from BaseClasses import ItemClassification, Region, Entrance, MultiWorld
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from .Items import ItbItem, itb_items, itb_trap_items, itb_progression_items, itb_filler_items
from .Locations import itb_locations, ItbLocation
from .Logic import can_beat_the_game
from .Options import itb_options
from .achievement.Achievements import achievements_by_squad
from .squad import Squad
from .squad.Squads import shuffle_teams, squad_names, vanilla_squads


class IntoTheBreachWorld(World):
    """A strategy turn based game"""
    game = "Into the Breach"
    option_definitions = itb_options

    base_id = 6777699702823011  # thanks random.org

    item_name_to_id = {name: id for
                       id, name in enumerate(itb_items, base_id)}
    locations = itb_locations
    location_name_to_id = {name: id for
                           id, name in enumerate(locations, base_id)}

    item_name_groups = {}
    required_server_version = (0, 4, 2)

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.squads: Optional[dict[str, Squad]] = None

    def generate_early(self) -> None:
        if self.multiworld.randomize_squads[self.player]:
            self.squads = shuffle_teams(self.random)
        else:
            self.squads = vanilla_squads()

    def create_item(self, item: str):
        if item == "Unlock Hive":
            classification = ItemClassification.progression_skip_balancing
        elif item in itb_progression_items:
            classification = ItemClassification.progression
        elif item in itb_trap_items:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        return ItbItem(item, classification, self.item_name_to_id[item], self.player)

    def get_filler_item_name(self) -> str:
        if self.random.randint(1, 3) == 1:
            return self.random.choice(itb_trap_items)
        else:
            return self.random.choice(itb_filler_items)

    def create_location(self, name: str, region):
        return ItbLocation(self.player, name, self.location_name_to_id[name], region)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        if self.multiworld.custom_squad[self.player]:
            squad_region = Region("Custom Squad", self.player, self.multiworld)
            entrance = Entrance(self.player, "Use custom squad", menu)
            menu.exits.append(entrance)
            entrance.connect(squad_region)

            self.multiworld.regions.append(squad_region)
            for achievement_name in itb_locations:
                squad_region.locations.append(self.create_location(achievement_name, squad_region))

        else:
            for squad_name in squad_names:
                squad_region = Region(squad_name + " Squad", self.player, self.multiworld)
                for achievement_name in achievements_by_squad[squad_name]:
                    squad_region.locations.append(self.create_location(achievement_name, squad_region))

                entrance = Entrance(self.player, "Use squad " + squad_name, menu)
                if squad_name != "Rift Walkers":
                    set_rule(entrance, lambda state, squad=squad_name: state.has(squad, self.player))
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

        while locations_count > item_count:
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))
            item_count += 1

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: can_beat_the_game(state, self.player)

    def fill_slot_data(self) -> dict:
        result = {}
        if self.multiworld.custom_squad[self.player]:
            result["custom"] = True
        if self.multiworld.randomize_squads[self.player]:
            squads = {}
            for squad_name in self.squads:
                squad = []
                units = self.squads[squad_name].units
                for unit_name in units:
                    squad.append(units[unit_name]["Name"])
                squads[squad_name] = squad
            result["squads"] = squads
        return result

    @classmethod
    def stage_write_spoiler(cls, multiworld: MultiWorld, spoiler_handle: TextIO):
        players = multiworld.get_game_players(cls.game)
        header = False
        for player in players:
            if multiworld.randomize_squads[player]:
                if not header:
                    spoiler_handle.write("\n\nInto the Breach Squads:\n")
                    header = True
                name = multiworld.get_player_name(player)
                spoiler_handle.write("\n" + name + " : \n")
                squads = multiworld.worlds[player].squads
                for squad_name in squads:
                    squad: Squad = squads[squad_name]
                    names = []
                    for unit_name in squad.units:
                        names.append(unit_name)
                    spoiler_handle.write(
                        squad_name + " : " + names[0] + ", " + names[1] + ", " + names[2] + "\n")
