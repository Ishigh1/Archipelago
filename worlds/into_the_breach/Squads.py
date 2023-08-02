import copy

from .Units import unit_table
from random import Random

squad_names = [
    "Rift Walkers",
    "Rusting Hulks",
    "Zenith Guard",
    "Blitzkrieg",
    "Steel Judoka",
    "Flame Behemoths",
    "Frozen Titans",
    "Hazardous Mechs"
]

class_names = [
    "Prime",
    "Brute",
    "Ranged",
    "Science"
]


def shuffle_teams(random: Random) -> dict[str, list[dict]]:
    all_units = {}
    for class_name in class_names:
        class_units = []
        for unit_name in unit_table:
            unit = unit_table[unit_name]
            if class_name in unit["Type"] and "Disabled" not in unit:
                class_units.append(unit)
        all_units[class_name] = class_units

    squad_amount = len(squad_names)

    """Returns a list of squadAmount teams composed of 3 unique units from different classes"""
    remaining_units = copy.deepcopy(all_units)

    not_picked = []
    for (class_name, units) in remaining_units.items():
        if len(units) < squad_amount:
            not_picked += [class_name] * (squad_amount - len(units))

    while len(not_picked) < squad_amount:
        not_picked.append(class_names[random.randint(0, 3)])

    random.shuffle(not_picked)

    squads = {}
    for squad_name in squad_names:
        rejected_class_name = not_picked.pop()
        squad = []
        for class_name in class_names:
            if class_name != rejected_class_name:
                class_units = remaining_units[class_name]
                unit = class_units.pop(random.randint(0, len(class_units) - 1))
                squad.append(unit)
        squads[squad_name] = squad
    return squads


def vanilla_squads() -> dict[str, list[dict]]:
    result = {}
    for squad_name in squad_names:
        squad = []
        for unit_name in unit_table:
            unit = unit_table[unit_name]
            if unit["Squad"] == squad_name:
                squad.append(unit)
        result[squad_name] = squad
    return result
