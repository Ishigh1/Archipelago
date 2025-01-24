# The SAT version
from random import Random
from typing import Tuple

from . import Squad
from .SquadInfo import class_names
from .TagSystem import tag_implications
from .Units import unit_table, tags_from_unit
from ..achievement.Achievements import achievement_info_table


def shuffle_teams(random: Random, filtered_squad_names: list[str], unit_plando: dict[str, str]) -> dict[str, Squad]:
    from pysat.solvers import Glucose42
    units_per_tag: dict[str, set] = {}
    units_per_class: dict[str, list] = {}

    for mech_class in class_names:
        units_per_class[mech_class] = []

    for unit_name in unit_table:
        unit = unit_table[unit_name]
        if "Disabled" not in unit:
            units_per_class[unit["Type"][0]].append(unit_name)
            tags = tags_from_unit(unit)
            for tag in tags:
                if tag not in units_per_tag:
                    units_per_tag[tag] = set()
                units_per_tag[tag].add(unit_name)

    solver = Glucose42()
    squad_ids = {}
    for squad_id, squad_name in enumerate(filtered_squad_names):
        squad_ids[squad_name] = squad_id
    squad_count = len(filtered_squad_names)

    unit_ids = {}
    unit_name_from_id = {}
    for unit_id, unit_name in enumerate(unit_table, 1):
        unit_ids[unit_name] = unit_id
        unit_name_from_id[unit_id] = unit_name
    unit_count = len(unit_table)

    next_id = squad_count * (unit_count + 1)

    def get_unit_id_from_unit_and_squad_ids(unit_id: int, squad_id: int) -> int:
        return squad_id + unit_id * squad_count

    def get_unit_id_from_unit_and_squad_names(unit_name: str, squad_name: str) -> int:
        return get_unit_id_from_unit_and_squad_ids(unit_ids[unit_name], squad_ids[squad_name])

    def get_unit_and_squad_names_from_unit_id(solver_id: int) -> Tuple[str, str]:
        unit_id = solver_id // squad_count
        squad_id = solver_id % squad_count
        if unit_id == 0:
            squad_id -= 1
            unit_id = squad_count
        return unit_name_from_id[unit_id], filtered_squad_names[squad_id]

    # Unit uniqueness
    for unit_id in range(1, unit_count + 1):
        for squad_id_1 in range(squad_count - 1):
            for squad_id_2 in range(squad_id_1 + 1, squad_count):
                solver.add_clause([-get_unit_id_from_unit_and_squad_ids(unit_id, squad_id_1), -get_unit_id_from_unit_and_squad_ids(unit_id, squad_id_2)])

    if __debug__:
        assert solver.solve()

    # A unit type uniqueness
    for squad_id in range(squad_count):
        for unit_id_1 in range(1, unit_count + 1):
            unit_1 = unit_table[unit_name_from_id[unit_id_1]]
            if "Disabled" in unit_1:
                solver.add_clause([-get_unit_id_from_unit_and_squad_ids(unit_id_1, squad_id)])
            else:
                unit_type_1 = unit_1["Type"][0]
                for unit_id_2 in range(unit_id_1 + 1, unit_count + 1):
                    unit_2 = unit_table[unit_name_from_id[unit_id_2]]
                    if "Disabled" not in unit_2:
                        unit_type_2 = unit_2["Type"][0]
                        if unit_type_1 == unit_type_2:
                            solver.add_clause(
                                [-get_unit_id_from_unit_and_squad_ids(unit_id_1, squad_id), -get_unit_id_from_unit_and_squad_ids(unit_id_2, squad_id)])

    if __debug__:
        assert solver.solve()

    # At least 3 units per squad
    # So the list of all units -2 units always contain a unit in the squad
    for squad_id in range(squad_count):
        all_unit_ids = [get_unit_id_from_unit_and_squad_ids(unit_id, squad_id) for unit_id in range(1, unit_count + 1)]
        for unit_id_1 in range(1, unit_count):
            incomplete_clause = all_unit_ids.copy()
            incomplete_clause.remove(get_unit_id_from_unit_and_squad_ids(unit_id_1, squad_id))
            for unit_id_2 in range(unit_id_1 + 1, unit_count + 1):
                clause = incomplete_clause.copy()
                clause.remove(get_unit_id_from_unit_and_squad_ids(unit_id_2, squad_id))
                solver.add_clause(clause)

    if __debug__:
        assert solver.solve()

    # At most 3 units per squad
    # So each group of 4 different units must include one not in the squad
    for unit_name_1 in units_per_class["Prime"]:
        for unit_name_2 in units_per_class["Brute"]:
            for unit_name_3 in units_per_class["Ranged"]:
                for unit_name_4 in units_per_class["Science"]:
                    for squad_name in filtered_squad_names:
                        solver.add_clause([-get_unit_id_from_unit_and_squad_names(unit_name_1, squad_name),
                                           -get_unit_id_from_unit_and_squad_names(unit_name_2, squad_name),
                                           -get_unit_id_from_unit_and_squad_names(unit_name_3, squad_name),
                                           -get_unit_id_from_unit_and_squad_names(unit_name_4, squad_name)])

    if __debug__:
        assert solver.solve()

    def add_clause(all_clauses: list[list], clause: list) -> bool:
        for existing_clause in all_clauses:
            for unit in existing_clause:
                if unit not in clause:
                    break
            else:
                return False  # superfluous clause

        removable_clauses = []
        for existing_clause in all_clauses:
            for unit in clause:
                if unit not in existing_clause:
                    break
            else:
                removable_clauses.append(existing_clause)

        for existing_clause in removable_clauses:
            all_clauses.remove(existing_clause)

        all_clauses.append(clause)
        return True

    def get_tag_clauses_from_achievement(achievement: dict) -> list[list[str]]:
        if achievement["required_tags"] is None:
            return []
        required_tags = list(achievement["required_tags"])
        for i in range(len(required_tags)):
            if isinstance(required_tags[i][-1], str):
                required_tags[i] = list(required_tags[i])
            else:
                if len(required_tags[i]) == 1:
                    del required_tags[i]
                else:
                    required_tags[i] = list(required_tags[i][:-1])

        current_line_number = 0
        while current_line_number < len(required_tags):
            current_tag_number = 0
            current_line = required_tags[current_line_number]
            while current_tag_number < len(current_line):
                current_tag = current_line[current_tag_number]
                if current_tag in tag_implications:
                    added_tags = []
                    for new_tag in tag_implications[current_tag]:
                        if new_tag not in current_line:
                            added_tags.append(new_tag)

                    if len(added_tags) > 0:
                        del required_tags[current_line_number]
                        for added_tag in added_tags:
                            if add_clause(required_tags, current_line + [added_tag]):
                                current_line_number = -1
                        if current_line_number == -1:
                            break
                        else:
                            required_tags.insert(current_line_number, current_line)
                current_tag_number += 1
            current_line_number += 1
        return required_tags

    # Add achievement constraints
    for achievement_name in achievement_info_table:
        achievement = achievement_info_table[achievement_name]
        if "required_tags" in achievement:
            tag_clauses = get_tag_clauses_from_achievement(achievement)
            squad_name = achievement["squad"]
            if squad_name not in filtered_squad_names:
                continue
            for tag_clause in tag_clauses:
                unit_clause = set()
                for tag in tag_clause:
                    if tag in units_per_tag:
                        unit_clause.update(units_per_tag[tag])
                solver.add_clause([get_unit_id_from_unit_and_squad_names(unit_name, squad_name) for unit_name in unit_clause])
                if __debug__:
                    assert solver.solve()

    all_unit_atoms = list(range(1, squad_count * (unit_count + 1)))
    random.shuffle(all_unit_atoms)

    for unit_name in unit_plando:
        forced_atom = get_unit_id_from_unit_and_squad_names(unit_name, unit_plando[unit_name])
        all_unit_atoms.remove(forced_atom)
        all_unit_atoms.append(forced_atom)

    assumptions = []
    for i in all_unit_atoms:
        new_assumptions = assumptions + [-i]
        status = solver.solve(new_assumptions)
        if status:
            assumptions = new_assumptions
        else:
            assumptions = assumptions + [i]

    randomized_squads = {}
    for solver_id in assumptions:
        if solver_id > 0:
            unit_name, squad_name = get_unit_and_squad_names_from_unit_id(solver_id)
            if squad_name not in randomized_squads:
                randomized_squads[squad_name] = Squad(squad_name)
            randomized_squads[squad_name].add_unit(unit_table[unit_name])

    return randomized_squads
