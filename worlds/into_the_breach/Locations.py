from typing import Iterator

from BaseClasses import Location
from .achievement.Achievements import achievement_table, achievements_by_squad


class ItbLocation(Location):
    game = "Into The Breach"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None, randomized=False):
        super(ItbLocation, self).__init__(player, name, code, parent)
        if randomized:
            self.access_rule = achievement_table[name].get_access_rule(player)
        self.event = False


def get_locations_names(filtered_squad_names: list[str]) -> Iterator[str]:
    for squad_name in filtered_squad_names:
        for achievement_name in achievements_by_squad[squad_name]:
            yield achievement_name