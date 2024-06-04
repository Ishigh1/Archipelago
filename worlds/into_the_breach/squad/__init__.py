from .TagSystem import expand_tags, add_tags
from .Units import unit_table, tags_from_unit
from .Weapons import weapon_table


class Squad:
    def __init__(self, name: str):
        self._cached = False
        self.units: dict[str, dict] = {}
        self.name = name
        self._tags: dict[str, int]

    def add_unit(self, unit: dict) -> bool:
        unit_name = unit["Name"]
        if unit_name not in self.units:
            self.units[unit_name] = unit
            self._cached = False
            return True
        else:
            return False

    def remove_unit(self, unit: dict) -> bool:
        unit_name = unit["Name"]
        if unit_name in self.units:
            del self.units[unit_name]
            self._cached = False
            return True
        else:
            return False

    def set_units(self, units: dict[str, dict]):
        if self.units != units:
            self._cached = False
        self.units = units

    def get_tags(self) -> dict[str, int]:
        if not self._cached:
            self._compute_tags()
        return self._tags

    def _compute_tags(self) -> None:
        self._cached = True

        tags = {}
        for unit_name in self.units:
            add_tags(tags, tags_from_unit(unit_table[unit_name]))

        self._tags = tags
