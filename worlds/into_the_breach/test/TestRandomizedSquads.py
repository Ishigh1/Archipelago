from BaseClasses import MultiWorld
from . import ItbTestBase
from ..squad import Squad
from ..squad.Squads import class_names


def get_squads(multiworld: MultiWorld) -> dict[str, Squad]:
    """
    A utility function to easily fetch the randomized squads
    """
    world = multiworld.worlds[1]
    return world.squads


class ItbRandomizedSquadsTest(ItbTestBase):
    options = {
        "randomize_squads": True
    }

    def test_one_pawn_per_class(self):
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            squad = squads[squad_name]
            class_set = set()
            for unit_name in squad.units:
                types = squad.units[unit_name]["Type"]
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
            for unit_name in squad.units:
                unit = squad.units[unit_name]
                if "Disabled" in unit:
                    self.assertFalse(squad.units[unit_name]["Disabled"])

    def test_3_units_by_squad(self):
        squads = get_squads(self.multiworld)
        for squad_name in squads:
            self.assertEqual(len(squads[squad_name].units), 3,
                             f"{squad_name} has more than 3 units ({squads[squad_name].units}")

    def test_no_duplicate_unit(self):
        squads = get_squads(self.multiworld)
        units = set()
        for squad_name in squads:
            for unit_name in squads[squad_name].units:
                self.assertNotIn(unit_name, units, "Duplicate unit found")
                units.add(unit_name)