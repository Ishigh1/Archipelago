from typing import Iterator

from BaseClasses import Location, Region
from .achievement.Achievements import achievements_by_squad


class ItbLocation(Location):
    game = "Into The Breach"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name: str, code: int, parent: Region):
        super(ItbLocation, self).__init__(player, name, code, parent)
        self.event = False


def get_locations_names(filtered_squad_names: list[str]) -> Iterator[str]:
    for squad_name in filtered_squad_names:
        for achievement_name in achievements_by_squad[squad_name]:
            yield achievement_name

    for i in range(1, 5):
        yield f"Island {i} cleared"
