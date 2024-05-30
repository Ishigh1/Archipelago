from typing import Iterator

from BaseClasses import Location
from .achievement.Achievements import achievement_table, achievements_by_squad


class ItbLocation(Location):
    game = "Into The Breach"

    # override constructor to automatically mark event locations as such
    def __init__(self, world: "IntoTheBreachWorld", player: int, name="", code=None, parent=None, custom=False):
        super(ItbLocation, self).__init__(player, name, code, parent)
        if custom:
            self.access_rule = achievement_table[name].get_custom_access_rule(player)
        else:
            rule = achievement_table[name].get_core_access_rule(world, player)
            if rule is not None:
                self.access_rule = achievement_table[name].get_core_access_rule(world, player)
        self.event = False


def get_locations_names(filtered_squad_names: list[str]) -> Iterator[str]:
    for squad_name in filtered_squad_names:
        for achievement_name in achievements_by_squad[squad_name]:
            yield achievement_name