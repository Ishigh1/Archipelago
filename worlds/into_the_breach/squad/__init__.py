from .TagSystem import add_tag, expand_tags
from .Units import unit_table
from .Weapons import weapon_table


class Squad:
    def __init__(self, name: str):
        self._cached = False
        self.units: dict[str, dict] = {}
        self.name = name

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

    def _compute_tags(self):
        tags = dict()
        self._cached = True
        for unit_name in self.units:
            unit = self.units[unit_name]
            for trait in unit["Traits"]:
                add_tag(tags, trait, 0)

            for weapon_name in unit["Weapons"]:
                weapon_tags = weapon_table[weapon_name]["Tags"]
                for tag, value in weapon_tags.items():
                    add_tag(tags, tag, value)
            expand_tags(tags)
        self._tags = tags
