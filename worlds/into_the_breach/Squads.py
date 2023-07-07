import copy
from .Locations import itb_locations

all_units = {
    "Prime": {
        "PunchMech",
        "JudoMech",
        "FlameMech",
        "LaserMech",
        "GuardMech",
        "ElectricMech",
        "LeapMech",
        "BeetleMech",  # Technically a Vek, but I don't like making a 5th class
        "RockMech",  # Not in any squad, but still in the files, why not use it ?
        # "TinyheadMech", # Not implemented, it's BottlecapMech weaker
        "BulkMech",
        "NeedleMech",
        "InfernoMech",
        "BottlecapMech"
    },
    "Brute": {
        "TankMech",
        "JetMech",
        "ChargeMech",
        "MirrorMech",
        "WallMech",
        "UnstableTank",
        "HornetMech",  # Technically a Vek, but I don't like making a 5th class
        "RocketcrabMech",  # Not implemented, but might as well add it
        "PierceMech",
        "DoubletankMech",
    },
    "Ranged": {
        "ArtiMech",
        "DStrikeMech",
        "RocketMech",
        "IgniteMech",
        "IceMech",
        "RockartMech",
        "ScarabMech",  # Technically a Vek, but I don't like making a 5th class
        "TiltMech",  # Not implemented, but might as well add it
        "BomblingMech",
        "ScorpioMech",
        "SmokeMech",
        # "NapalmMech2", # Not implemented, same name as the science one, just less interesting
        "TrimissileMech",
    },
    "Science": {
        "GravMech",
        "PulseMech",
        "TeleMech",
        "ScienceMech",
        "NanoMech",
        "ExchangeMech",
        "FourwayMech",
        "SupermanMech",
        "NapalmMech",
        "PlacerMech",  # Not implemented, but might as well add it
        "HydrantMech",
    },
}
class_names = [
    "Prime",
    "Brute",
    "Ranged",
    "Science"
]

squad_amount = 14


def shuffle_teams(random):
    """Returns a list of squadAmount teams composed of 3 unique units from different classes"""
    remaining_units = copy.deepcopy(all_units)

    # The obvious issue here is that I can't just take 3 units 14 times, I could take 10 times the sames and softlock
    # The solution I use is to consider which class I need to not pick and how many times, and fill the list with
    # random ones after
    not_picked = []
    for (class_name, units) in remaining_units.items():
        if len(units) < squad_amount:
            not_picked += [class_name] * (squad_amount - len(units))

    # As I'm writing this, should be "Prime" * 1, "Brute" * 4, "Ranged" * 2, "Science" * 3

    while len(not_picked) < squad_amount:
        not_picked.append(class_names[random.randint(0, 3)])

    random.shuffle(not_picked)

    squads = {}
    for squad_name in itb_locations:
        rejected_class_name = not_picked.pop()
        squad = []
        for class_name in class_names:
            if class_name != rejected_class_name:
                class_units = remaining_units[class_name]
                unit = random.choice(list(class_units))
                class_units.remove(unit)
                squad.append(unit)
        squads[squad_name] = squad
    return squads
