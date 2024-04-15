from typing import Callable

from . import Squad
from .SquadInfo import class_names, squad_names
from .Units import unit_table
from random import Random
from ..achievement.AchievementHelper import can_get_all_achievements


def shuffle_teams(random: Random) -> dict[str, Squad]:
    """Returns a list of squadAmount teams composed of 3 unique units from different classes"""
    units_by_class = {}  # dict class_name -> list_of_units, only the relevant ones are kept
    units = {}  # dict unit_name -> unit, only the relevant ones are kept
    for class_name in class_names:
        class_units = []
        for unit_name in unit_table:
            unit = unit_table[unit_name]
            if class_name in unit["Type"] and "Disabled" not in unit:
                class_units.append(unit)
                units[unit_name] = unit
        random.shuffle(class_units)
        units_by_class[class_name] = class_units

    squad_amount = len(squad_names)
    while True:
        not_picked = []  # list of classes to not pick
        for (class_name, class_units) in units_by_class.items():
            if len(class_units) < squad_amount:
                not_picked += [class_name] * (squad_amount - len(class_units))

        while len(not_picked) < squad_amount:
            not_picked.append(class_names[random.randint(0, 3)])

        # Order not_picked based on the number of available units
        not_picked = sorted(not_picked, key=lambda class_name: len(units_by_class[class_name]))

        shuffled_squad_names = random.sample(squad_names, len(squad_names))
        squads = {}  # dict squad_name -> squad, also the return value
        for squad_name in shuffled_squad_names:
            squad = Squad(squad_name)
            squad.set_units(units.copy())
            squads[squad_name] = squad

        if select_units(not_picked, random, squads, units_by_class):
            break
    return squads


def select_units(not_picked: [str], random: Random, squads: dict[str, Squad],
                 units_by_class: dict[str, [dict]]) -> bool:
    squads_to_handle = list(squads.keys())
    random.shuffle(squads_to_handle)  # Last ones in line are less likely to have units used in other's achievements

    if not select_units_for_squad(not_picked, random, squads, units_by_class, squads_to_handle):
        return False
    return True


def select_units_for_squad(not_picked: [str], random: Random, squads: dict[str, Squad],
                           units_by_class: dict[str, [dict]], squads_to_handle: [str]) -> bool:
    if len(squads_to_handle) == 0:
        return True

    squad_name = squads_to_handle.pop()
    squad = squads[squad_name]
    units = squad.units.copy()

    tried_to_not_pick = set()
    for i in range(len(not_picked)):
        forbidden_class = not_picked[i]
        if forbidden_class not in tried_to_not_pick:
            forbidden_units = units_by_class[forbidden_class]
            for unit in forbidden_units:
                squad.remove_unit(unit)

            if can_get_all_achievements(squad):
                new_forbidden_class_list = not_picked.copy()
                del new_forbidden_class_list[i]

                other_class_names = []
                for class_name in class_names:
                    if class_name != forbidden_class:
                        other_class_names.append(class_name)
                random.shuffle(
                    other_class_names)  # The last one of this list is more likely to be essential for the achievements

                if select_unit_for_class(0, random, squad, squads_to_handle, units_by_class,
                                         other_class_names, squads,
                                         lambda: select_units_for_squad(not_picked, random, squads, units_by_class,
                                                                        squads_to_handle)):
                    assert len(squad.units) == 3
                    return True

            tried_to_not_pick.add(forbidden_class)
            squad.set_units(units)
    squads_to_handle.append(squad_name)
    return False


def select_unit_for_class(class_id: int, random: Random, squad: Squad,
                          squads_to_handle: [str], units_by_class: dict[str, [dict]], other_class_names: [str],
                          squads: dict[str, Squad], after: Callable[[], bool]) -> bool:
    if class_id == len(other_class_names):
        return after()
    class_name = other_class_names[class_id]
    class_units = units_by_class[class_name].copy()

    units = {
        "self": squad.units.copy()
    }
    for squad_name in squads_to_handle:
        units[squad_name] = squads[squad_name].units.copy()

    for unit in class_units:
        squad.remove_unit(unit)

    units["ready"] = squad.units
    fails = 0

    for i in range(len(class_units)):
        squad.set_units(units["ready"].copy())
        unit = class_units[i]
        squad.add_unit(unit)
        if can_get_all_achievements(squad):
            for other_squad_name in squads_to_handle:
                other_squad = squads[other_squad_name]
                other_squad.remove_unit(unit)
                if not can_get_all_achievements(other_squad):
                    break
            else:
                del units_by_class[class_name][i]
                if select_unit_for_class(class_id + 1, random, squad, squads_to_handle,
                                         units_by_class, other_class_names, squads, after):
                    assert len(squad.units) == 3
                    return True
                units_by_class[class_name] = class_units.copy()
                fails = fails + 1
            for squad_name in squads_to_handle:
                squads[squad_name].set_units(units[squad_name].copy())
            if fails == 5:  # probably a bad pick, let's skip
                break
    squad.set_units(units["self"])
    return False


def vanilla_squads() -> dict[str, Squad]:
    result = {}
    for squad_name in squad_names:
        result[squad_name] = Squad(squad_name)
    for unit_name in unit_table:
        unit = unit_table[unit_name]
        squad_name = unit["Squad"]
        if squad_name in result:
            result[squad_name].add_unit(unit)
    return result
