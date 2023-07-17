from BaseClasses import Location


class MyGameLocation(Location):
    game = "Into The Breach"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None):
        super(MyGameLocation, self).__init__(player, name, code, parent)
        self.event = code is None


itb_locations = {
    "Rift Walkers":
        [
            # Drown 3 enemies in water in a single battle with the Rift Walkers squad
            "Watery Grave",
            # Kill an enemy 5 or more tiles away with a Dash Punch with the Rift Walkers squad
            "Ramming Speed",
            # Complete 1st Corporate Island with the Rift Walkers squad
            "Island Secure",
        ],
    "Rusting Hulks":
        [
            # Overpower your Power Grid twice by earning or buying Power when it is full with the Rusting Hulks squad
            "Overpowered",
            # Deal 12 damage with Electric Smoke in a single battle with the Rusting Hulks squad
            "Stormy Weather",
            # Take no Mech or Building Damage in a single battle with the Rusting Hulks squad
            "Perfect Battle",
        ],
    "Zenith Guard":
        [
            "Get Over Here",
            "Glittering C-Beam",
            "Shield Mastery",
        ],
    "Blitzkrieg":
        [
            "Chain Attack",
            "Lightning War",
            "Hold the Line",
        ],
    "Steel Judoka":
        [
            "Unbreakable",
            "Unwitting Allies",
            "Mass Displacement",
        ],
    "Flame Behemoths":
        [
            "Quantum Entaglement",
            "Scorched Earth",
            "This is Fine",
        ],
    "Frozen Titans":
        [
            "Cryo Expert",
            "Pacifist",
            "Trick Shot",
        ],
    "Hazardous Mechs":
        [
            "Healing",
            "Immortal",
            "Overkill",
        ]
}
