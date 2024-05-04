from .TagSystem import expand_tags
from .Units import unit_table
from .Weapons import weapon_table

class Squad:
    def __init__(self, name: str):
        self._cached = False
        self.units: dict[str, dict] = {}
        self.name = name
        self._tags: set[str]

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

    def get_tags(self) -> set[str]:
        if not self._cached:
            self._compute_tags()
        return self._tags

    def _compute_tags(self):
        self._cached = True

        # Pre-fetch traits and weapon tags
        unit_traits = self.units.values()
        # Flatten and collect individual weapon tags
        tags = {tag for unit_name in self.units for weapon_name in self.units[unit_name]["Weapons"]
                for tag in weapon_table[weapon_name]["Tags"].keys()}

        for unit in unit_traits:
            for trait in unit["Traits"]:
                tags.add(trait)

        expand_tags(tags)
        self._tags = tags
