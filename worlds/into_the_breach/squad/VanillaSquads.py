from . import Squad
from .Units import unit_table


def vanilla_squads(filtered_squad_names: list[str]) -> dict[str, Squad]:
    result = {}
    for squad_name in filtered_squad_names:
        result[squad_name] = Squad(squad_name)
    for unit_name in unit_table:
        unit = unit_table[unit_name]
        squad_name = unit["Squad"]
        if squad_name in result:
            result[squad_name].add_unit(unit)
    return result
