import unittest

from BaseClasses import MultiWorld
from . import ItbTestBase
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

    def test_one_pawn_per_class(self):
        squads = get_squads(self.multiworld)
        for squad_name in squads:
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

    def test_no_disabled_unit(self):
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            squad = squads[squad_name]
            for unit_name in squad:
                unit = unit_table[unit_name]
                if "Disabled" in unit:
                    self.assertFalse(unit["Disabled"])

    def test_3_units_by_squad(self):
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            self.assertEqual(len(squads[squad_name]), 3,
                             f"{squad_name} has more than 3 units ({squads[squad_name]}")

    @unittest.skip("Currently disabled to improve performance")
    def test_no_duplicate_unit(self):
        squads = get_squads(self.multiworld)
        units = set()
        for squad_name in squads:
            for unit_name in squads[squad_name]:
                self.assertNotIn(unit_name, units, "Duplicate unit found")
                units.add(unit_name)
