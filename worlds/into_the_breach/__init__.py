import logging
from typing import TextIO, Optional

from BaseClasses import ItemClassification, Region, Entrance, MultiWorld, CollectionState
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from .Items import ItbItem, itb_items, itb_trap_items, itb_progression_items, itb_filler_items, itb_squad_items, itb_upgrade_items
from .Locations import ItbLocation, get_locations_names
from .Logic import can_beat_the_game
from .Options import IntoTheBreachOptions
from .achievement.Achievements import achievements_by_squad
from .squad import Squad
from .squad.SquadInfo import squad_names
from .squad.SquadRando import shuffle_teams
from .squad.VanillaSquads import vanilla_squads


class IntoTheBreachWorld(World):
    """A strategy turn based game"""
    game = "Into the Breach"
    options_dataclass = IntoTheBreachOptions
    options: IntoTheBreachOptions

    base_id = 6777699702823011  # thanks random.org

    item_name_to_id = {name: id for
                       id, name in enumerate(itb_items, base_id)}
    locations = get_locations_names(squad_names)
    location_name_to_id = {name: id for
                           id, name in enumerate(locations, base_id)}

    item_name_groups = {}

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.squads: Optional[dict[str, Squad]] = None

    def generate_early(self) -> None:
        squad_names_copy = squad_names.copy()
        filtered_squad_names = []
        additional_squads = self.options.squad_number.value
        has_starting_squad = False
        for item in self.options.start_inventory_from_pool.value:
            if item in squad_names_copy:
                filtered_squad_names.append(item)
                squad_names_copy.remove(item)
                additional_squads -= 1
                has_starting_squad = True

        if additional_squads > 0:
            self.random.shuffle(squad_names_copy)
            filtered_squad_names += squad_names_copy[0:additional_squads]
            if not has_starting_squad:
                self.options.start_inventory_from_pool.value[filtered_squad_names[0]] = 1
        elif additional_squads < 0:
            player_name = self.multiworld.player_name[self.player]
            logging.warning(f"player {self.player} ({player_name}) has more squads in the start inventory than they asked for")

        if self.options.randomize_squads:
            self.squads = shuffle_teams(self.random, filtered_squad_names)
        else:
            self.squads = vanilla_squads(filtered_squad_names)

    def create_item(self, item: str):
        if item in itb_progression_items:
            classification = ItemClassification.progression
        elif item in itb_trap_items:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        ap_item = ItbItem(item, classification, self.item_name_to_id[item], self.player)
        if classification == ItemClassification.progression:
            if item in itb_squad_items:
                ap_item.squad = True
        return ap_item

    def get_filler_item_name(self) -> str:
        if self.random.randint(1, 5) == 1:
            return self.random.choice(itb_trap_items)
        else:
            return self.random.choice(itb_filler_items)

    def create_location(self, name: str, region: Region, randomized: bool):
        return ItbLocation(self.player, name, self.location_name_to_id[name], region, randomized)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        if self.options.custom_squad:
            squad_region = Region("Custom Squad", self.player, self.multiworld)
            entrance = Entrance(self.player, "Use custom squad", menu)
            menu.exits.append(entrance)
            entrance.connect(squad_region)

            self.multiworld.regions.append(squad_region)
            for achievement_name in get_locations_names(list(self.squads)):
                squad_region.locations.append(self.create_location(achievement_name, squad_region, True))
        else:
            for squad_name in self.squads:
                squad_region = Region(squad_name + " Squad", self.player, self.multiworld)
                for achievement_name in achievements_by_squad[squad_name]:
                    squad_region.locations.append(self.create_location(achievement_name, squad_region, False))

                entrance = Entrance(self.player, "Use squad " + squad_name, menu)
                set_rule(entrance, lambda state, squad=squad_name: state.has(squad, self.player))
                menu.exits.append(entrance)
                entrance.connect(squad_region)

                self.multiworld.regions.append(squad_region)

    def create_items(self) -> None:
        item_count = 0
        for item_name in itb_upgrade_items:
            if item_name == "3 Starting Grid Defense":
                count = 5
            elif item_name == "2 Starting Grid Power":
                count = 2
            else:
                raise Exception()

            item_count += count
            for i in range(count):
                item = self.create_item(item_name)
                self.multiworld.itempool.append(item)
        for squad_name in self.squads:
            item = self.create_item(squad_name)
            if squad_name in self.options.start_inventory_from_pool.value:
                self.multiworld.push_precollected(item)
                self.options.start_inventory_from_pool.value[squad_name] = 0
            else:
                item_count += 1
                self.multiworld.itempool.append(item)

        locations_count = len([location
                               for location in self.multiworld.get_locations(self.player)
                               if not location.event])

        while locations_count > item_count:
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))
            item_count += 1

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: (
                state.prog_items[self.player]["squads"] * 3 >= self.options.required_achievements.value * len(self.squads) // 100
                and can_beat_the_game(state, self.player))

    def fill_slot_data(self) -> dict:
        result = {}
        if self.options.custom_squad:
            result["custom"] = True
        if self.options.randomize_squads:
            squads = {}
            for squad_name in self.squads:
                squad = []
                units = self.squads[squad_name].units
                for unit_name in units:
                    squad.append(units[unit_name]["Name"])
                squads[squad_name] = squad
            result["squads"] = squads
        result["required_achievements"] = self.options.required_achievements.value * len(self.squads) // 100
        return result

    @classmethod
    def stage_write_spoiler(cls, multiworld: MultiWorld, spoiler_handle: TextIO):
        players = multiworld.get_game_players(cls.game)
        header = False
        for player in players:
            world: IntoTheBreachWorld = multiworld.worlds[player]
            if world.options.randomize_squads:
                if not header:
                    spoiler_handle.write("\n\nInto the Breach Squads:\n")
                    header = True
                name = multiworld.get_player_name(player)
                spoiler_handle.write("\n" + name + " : \n")
                squads = world.squads
                for squad_name in squads:
                    squad: Squad = squads[squad_name]
                    names = []
                    for unit_name in squad.units:
                        names.append(unit_name)
                    spoiler_handle.write(
                        squad_name + " : " + names[0] + ", " + names[1] + ", " + names[2] + "\n")

    def collect(self, state: CollectionState, item: ItbItem) -> bool:
        change = super().collect(state, item)
        if change:
            if item.squad:
                state.prog_items[self.player]["squads"] += 1
        return change

    def remove(self, state: CollectionState, item: ItbItem) -> bool:
        change = super().remove(state, item)
        if change:
            if item.squad:
                state.prog_items[self.player]["squads"] -= 1
        return change
