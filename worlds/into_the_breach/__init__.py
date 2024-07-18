import logging
from typing import TextIO, Optional

from BaseClasses import ItemClassification, Region, Entrance, MultiWorld, CollectionState
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from .Items import ItbItem, itb_items, itb_trap_items, itb_progression_items, itb_filler_items, itb_squad_items, \
    itb_upgrade_items, itb_common_trap_items, itb_uncommon_trap_items, itb_legendary_trap_items
from .Locations import ItbLocation, get_locations_names
from .Logic import core_function, can_get_5_cores
from .Options import IntoTheBreachOptions
from .achievement.Achievements import achievements_by_squad, achievement_table
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
    locations_names = get_locations_names(squad_names)
    location_name_to_id = {name: id for
                           id, name in enumerate(locations_names, base_id)}

    item_name_groups = {
        "Starting Grid Power": [
            "1 Starting Grid Power",
            "2 Starting Grid Power"
        ],
        "Squad": itb_squad_items,
        "Upgrade": itb_upgrade_items,
        "Traps": itb_trap_items,
    }

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.required_achievements = 0
        self.starting_squads = []
        self.squads: Optional[dict[str, Squad]] = None
        self.achievements: list[ItbLocation] = []

    def generate_early(self) -> None:
        squad_names_copy = squad_names.copy()
        filtered_squad_names = []
        additional_squads = self.options.squad_number.value
        unit_plando = self.options.unit_plando.value
        for item in self.options.start_inventory_from_pool.value:
            if item in squad_names_copy:
                filtered_squad_names.append(item)
                squad_names_copy.remove(item)
                additional_squads -= 1
                self.starting_squads.append(item)
        for item in self.starting_squads:
            del self.options.start_inventory_from_pool.value[item]

        for unit in unit_plando:
            if additional_squads == 0:
                break
            squad_name = unit_plando[unit]
            if squad_name not in filtered_squad_names:
                filtered_squad_names.append(squad_name)
                squad_names_copy.remove(squad_name)

        if additional_squads >= 0:
            self.random.shuffle(squad_names_copy)
            filtered_squad_names += squad_names_copy[0:additional_squads]
            if len(self.starting_squads) == 0:
                self.starting_squads.append(filtered_squad_names[0])
        elif additional_squads < 0:
            logging.warning(f"Player {self.player} ({self.player_name}) "
                            f"has more squads in the start inventory than they asked for")

        if self.options.randomize_squads:
            self.squads = shuffle_teams(self.random, filtered_squad_names, unit_plando)
            for unit_name in unit_plando:
                squad_name = unit_plando[unit_name]
                if squad_name not in self.squads:
                    logging.warning(f"Player {self.player} ({self.player_name}) "
                                    f"unit plando couldn't fully work, {squad_name} was excluded")
                elif unit_name in self.squads[squad_name].units:
                    logging.warning(f"Player {self.player} ({self.player_name}) "
                                    f"unit plando couldn't fully work, {unit_name} couldn't fit in {squad_name}")
        else:
            if len(unit_plando) > 0:
                logging.warning(f"Player {self.player} ({self.player_name}) had unit plando active but not squad rando")
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
            elif item == "1 Starting Grid Power":
                ap_item.start_power = 1
            elif item == "2 Starting Grid Power":
                ap_item.start_power = 2
        return ap_item

    def get_filler_item_name(self) -> str:
        """
        50% filler
        30% common trap
        15% uncommon trap
        5% legendary trap
        """
        r = self.random.randint(1, 20)
        if r <= 10:
            return self.random.choice(itb_filler_items)
        elif r <= 16:
            return self.random.choice(itb_common_trap_items)
        elif r <= 19:
            return self.random.choice(itb_uncommon_trap_items)
        else:
            return self.random.choice(itb_legendary_trap_items)

    def create_location(self, name: str, region: Region):
        return ItbLocation(self.player, name, self.location_name_to_id[name], region)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        if self.options.custom_squad:
            squad_region = Region("Custom Squad", self.player, self.multiworld)
            entrance = Entrance(self.player, "Use custom squad", menu)
            menu.exits.append(entrance)
            entrance.connect(squad_region)

            self.multiworld.regions.append(squad_region)
            for squad_name in self.squads:
                for achievement_name in achievements_by_squad[squad_name]:
                    location = self.create_location(achievement_name, squad_region)
                    self.achievements.append(location)
                    squad_region.locations.append(location)
                    location.access_rule = achievement_table[achievement_name].get_custom_access_rule(self.player)
        else:
            for squad_name in self.squads:
                squad_region = Region(f"{squad_name} Squad", self.player, self.multiworld)
                for achievement_name in achievements_by_squad[squad_name]:
                    location = self.create_location(achievement_name, squad_region)
                    self.achievements.append(location)
                    squad_region.locations.append(location)

                    achievement = achievement_table[achievement_name]
                    rule = achievement.get_core_access_rule(self, self.player)
                    if rule is not None:
                        location.access_rule = rule

                entrance = Entrance(self.player, f"Use squad {squad_name}", menu)
                set_rule(entrance, lambda state, squad=squad_name: state.has(squad, self.player))
                menu.exits.append(entrance)
                entrance.connect(squad_region)

                self.multiworld.regions.append(squad_region)

        previous_island = menu
        for i in range(1, 5):
            new_island = Region(f"Clear island {i}", self.player, self.multiworld)
            new_island.locations.append(self.create_location(f"Island {i} cleared", new_island))
            entrance = Entrance(self.player, f"Clear island {i}", previous_island)
            if i > 1:
                rule = core_function[i]
                set_rule(entrance, lambda state, island_rule=rule: island_rule(state, self.player))
            menu.exits.append(entrance)
            entrance.connect(new_island)
            self.multiworld.regions.append(new_island)
            previous_island = new_island

    def create_items(self) -> None:
        item_count = 0
        for item_name in itb_upgrade_items:
            if item_name == "3 Starting Grid Defense":
                count = 5
            elif item_name == "2 Starting Grid Power":
                if len(self.squads) >= 7:
                    continue
                count = 2
            elif item_name == "1 Starting Grid Power":
                if len(self.squads) < 7:
                    continue
                count = 4
            else:
                count = 1

            item_count += count
            for i in range(count):
                item = self.create_item(item_name)
                self.multiworld.itempool.append(item)
        for squad_name in self.squads:
            item = self.create_item(squad_name)
            if squad_name in self.starting_squads:
                self.multiworld.push_precollected(self.create_item(squad_name))
            else:
                item_count += 1
                self.multiworld.itempool.append(item)

        locations_count = len([location for location in self.multiworld.get_locations(self.player)])

        while locations_count > item_count:
            self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))
            item_count += 1

    def generate_basic(self) -> None:
        self.required_achievements = self.options.required_achievements.value * len(self.squads) * 3 // 100
        self.multiworld.completion_condition[self.player] = (
            lambda state: (state.prog_items[self.player]["squads"] * 3 >= self.required_achievements
                           and can_get_5_cores(state, self.player))
        )

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
        result["required_achievements"] = self.required_achievements
        result["difficulty"] = self.options.difficulty.value
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
                spoiler_handle.write(f"\n{name} : \n")
                squads = world.squads
                for squad_name in squads:
                    squad: Squad = squads[squad_name]
                    names = []
                    for unit_name in squad.units:
                        names.append(unit_name)
                    spoiler_handle.write(
                        f"{squad_name} : {names[0]}, {names[1]}, {names[2]}\n")

    def count_achievements(self, state: CollectionState):
        reachable_achievements = 0
        for location in self.achievements:
            if location.can_reach(state):
                reachable_achievements += 1
        return reachable_achievements

    def collect(self, state: CollectionState, item: ItbItem) -> bool:
        change = super().collect(state, item)
        if change:
            assert (item.advancement & ItemClassification.progression) != 0
            if item.squad:
                state.prog_items[self.player]["squads"] += 1
            state.prog_items[self.player]["start_power"] += item.start_power
        return change

    def remove(self, state: CollectionState, item: ItbItem) -> bool:
        change = super().remove(state, item)
        if change:
            assert (item.advancement & ItemClassification.progression) != 0
            if item.squad:
                state.prog_items[self.player]["squads"] -= 1
            state.prog_items[self.player]["start_power"] -= item.start_power
        return change
