from BaseClasses import Location
from .squad.Squads import squad_names
from .achievement.Achievements import achievement_table, achievements_by_squad


class ItbLocation(Location):
    game = "Into The Breach"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None):
        super(ItbLocation, self).__init__(player, name, code, parent)
        self.access_rule = achievement_table[name].get_access_rule(player)
        self.event = False


itb_locations: [str] = []
for squad_name in squad_names:
    itb_locations += achievements_by_squad[squad_name].keys()
