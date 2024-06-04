from unittest import TestCase

from ..squad.SquadRando import class_names
from ..squad.Units import unit_table


class TestData(TestCase):
    def test_one_class_per_unit(self) -> None:
        for unit_name in unit_table:
            unit = unit_table[unit_name]
            class_found = 0
            for class_name in unit["Type"]:
                if class_name in class_names:
                    class_found += 1
            self.assertEqual(class_found, 1)

    def test_unit_consistent_name(self) -> None:
        """
        Checks keys in unit_table are always equal to unit["Name"]
        """
        for unit_name in unit_table:
            unit = unit_table[unit_name]
            self.assertEqual(unit_name, unit["Name"])
