from BaseClasses import MultiWorld, CollectionState
from . import ItbTestBase
from .. import achievements_by_squad
from ..squad import unit_table
from ..squad.SquadRando import class_names


def get_squads(multiworld: MultiWorld) -> dict[str, [str]]:
    """
    A utility function to easily fetch the randomized squads
    """
    slotdata = multiworld.worlds[1].fill_slot_data()
    assert slotdata is not None
    return slotdata["squads"]


class ItbRandomizedSquadsTest(ItbTestBase):
    options = {
        "randomize_squads": True
    }

    def test_one_pawn_per_class(self) -> None:
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            with self.subTest("Squad should have no 3 different classes", squad=squad_name):
                squad = squads[squad_name]
                class_set = set()
                for unit_name in squad:
                    types = unit_table[unit_name]["Type"]
                    i = 0
                    class_name = types[0]
                    while class_name not in class_names:
                        i += 1
                        class_name = types[i]

                    self.assertNotIn(class_name, class_set)
                    class_set.add(class_name)

    def test_no_disabled_unit(self) -> None:
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            with self.subTest("Squad should have no disabled unit", squad=squad_name):
                squad = squads[squad_name]
                for unit_name in squad:
                    unit = unit_table[unit_name]
                    if "Disabled" in unit:
                        self.assertFalse(unit["Disabled"])

    def test_3_units_by_squad(self) -> None:
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            with self.subTest("Squad should have 3 units", squad=squad_name):
                self.assertEqual(len(squads[squad_name]), 3,
                                 f"{squad_name} has more than 3 units ({squads[squad_name]}")

    def test_no_duplicate_unit(self) -> None:
        squads = get_squads(self.multiworld)
        units = set()
        for squad_name in squads:
            with self.subTest("Squad should have no duplicate", squad=squad_name):
                for unit_name in squads[squad_name]:
                    self.assertNotIn(unit_name, units, "Duplicate unit found")
                    units.add(unit_name)

    def test_squad_can_beat_achievements(self) -> None:
        squads = get_squads(self.multiworld)
        state = CollectionState(self.multiworld)
        # First get all energy and defense
        for item in self.multiworld.itempool:
            if item.name not in squads:
                state.collect(item)

        for item in self.multiworld.itempool:
            if item.name in squads:
                state.collect(item)
                for achievement_name in achievements_by_squad[item.name]:
                    with self.subTest("Achievement should be reached", achievement=achievement_name):
                        self.assertTrue(state.can_reach_location(achievement_name, 1), f"{squads[item.name]} can't beat {achievement_name}")
                state.remove(item)
