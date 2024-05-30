# This file will list all the units, their categories, and their weapons
from .Weapons import weapon_table

unit_table = {
    # Rift Walkers (Squad Archive A)
    "PunchMech": {
        "Name": "PunchMech",
        "Type": ["Prime"],
        "Squad": "Rift Walkers",
        "Weapons": ["Titan Fist"],
        "Traits": [],
    },
    "TankMech": {
        "Name": "TankMech",
        "Type": ["Brute"],
        "Squad": "Rift Walkers",
        "Weapons": ["Taurus Cannon"],
        "Traits": [],
    },
    "ArtiMech": {
        "Name": "ArtiMech",
        "Type": ["Ranged"],
        "Squad": "Rift Walkers",
        "Weapons": ["Artemis Artillery"],
        "Traits": [],
    },

    # Rusting Hulks (Squad Rust A)
    "JetMech": {
        "Name": "JetMech",
        "Type": ["Brute"],
        "Squad": "Rusting Hulks",
        "Weapons": ["Aerial Bombs"],
        "Traits": ["Flying"],
    },
    "RocketMech": {
        "Name": "RocketMech",
        "Type": ["Ranged"],
        "Squad": "Rusting Hulks",
        "Weapons": ["Rocket Artillery", "Storm Generator"],
        "Traits": [],
    },
    "PulseMech": {
        "Name": "PulseMech",
        "Type": ["Science"],
        "Squad": "Rusting Hulks",
        "Weapons": ["Repulse"],
        "Traits": [],
    },

    # Zenith Guard (Squad Pinnacle A)
    "LaserMech": {
        "Name": "LaserMech",
        "Type": ["Prime"],
        "Squad": "Zenith Guard",
        "Weapons": ["Burst Beam"],
        "Traits": [],
    },
    "ChargeMech": {
        "Name": "ChargeMech",
        "Type": ["Brute"],
        "Squad": "Zenith Guard",
        "Weapons": ["Ramming Engines"],
        "Traits": [],
    },
    "ScienceMech": {
        "Name": "ScienceMech",
        "Type": ["Science"],
        "Squad": "Zenith Guard",
        "Weapons": ["Attraction Pulse", "Shield Projector"],
        "Traits": ["Flying"],
    },

    # Blitzkrieg (Squad Detritus A)
    "ElectricMech": {
        "Name": "ElectricMech",
        "Type": ["Prime"],
        "Squad": "Blitzkrieg",
        "Weapons": ["Electric Whip"],
        "Traits": [],
    },
    "WallMech": {
        "Name": "WallMech",
        "Type": ["Brute"],
        "Squad": "Blitzkrieg",
        "Weapons": ["Grappling Hook"],
        "Traits": ["Armor"],
    },
    "RockartMech": {
        "Name": "RockartMech",
        "Type": ["Ranged"],
        "Squad": "Blitzkrieg",
        "Weapons": ["Rock Accelerator"],
        "Traits": [],
    },

    # Steel Judoka (Squad Archive B)
    "JudoMech": {
        "Name": "JudoMech",
        "Type": ["Prime"],
        "Squad": "Steel Judoka",
        "Weapons": ["Vice Fist"],
        "Traits": ["Armor"],
    },
    "DStrikeMech": {
        "Name": "DStrikeMech",
        "Type": ["Ranged"],
        "Squad": "Steel Judoka",
        "Weapons": ["Cluster Artillery"],
        "Traits": [],
    },
    "GravMech": {
        "Name": "GravMech",
        "Type": ["Science"],
        "Squad": "Steel Judoka",
        "Weapons": ["Grav Well", "Vek Hormones"],
        "Traits": [],
    },

    # Flame Behemoths (Squad Rust B)
    "FlameMech": {
        "Name": "FlameMech",
        "Type": ["Prime"],
        "Squad": "Flame Behemoths",
        "Weapons": ["Flame Thrower"],
        "Traits": [],
    },
    "IgniteMech": {
        "Name": "IgniteMech",
        "Type": ["Ranged"],
        "Squad": "Flame Behemoths",
        "Weapons": ["Vulcan Artillery"],
        "Traits": [],
    },
    "TeleMech": {
        "Name": "TeleMech",
        "Type": ["Science"],
        "Squad": "Flame Behemoths",
        "Weapons": ["Teleporter"],
        "Traits": [],
    },

    # Frozen Titans (Squad Pinnacle B)
    "GuardMech": {
        "Name": "GuardMech",
        "Type": ["Prime"],
        "Squad": "Frozen Titans",
        "Weapons": ["Spartan Shield"],
        "Traits": [],
    },
    "MirrorMech": {
        "Name": "MirrorMech",
        "Type": ["Brute"],
        "Squad": "Frozen Titans",
        "Weapons": ["Janus Cannon"],
        "Traits": [],
    },
    "IceMech": {
        "Name": "IceMech",
        "Type": ["Ranged"],
        "Squad": "Frozen Titans",
        "Weapons": ["Cryo-Launcher"],
        "Traits": ["Flying"],
    },

    # Hazardous Mechs (Squad Detritus B)
    "LeapMech": {
        "Name": "LeapMech",
        "Type": ["Prime"],
        "Squad": "Hazardous Mechs",
        "Weapons": ["Hydraulic Legs"],
        "Traits": [],
    },
    "UnstableTank": {
        "Name": "UnstableTank",
        "Type": ["Brute"],
        "Squad": "Hazardous Mechs",
        "Weapons": ["Unstable Cannon"],
        "Traits": [],
    },
    "NanoMech": {
        "Name": "NanoMech",
        "Type": ["Science"],
        "Squad": "Hazardous Mechs",
        "Weapons": ["A.C.I.D. Projector", "Viscera Nanobots"],
        "Traits": ["Flying"],
    },

    # Secret Squad
    "BeetleMech": {
        "Name": "BeetleMech",
        "Type": ["Prime", "Vek"],
        "Squad": "Secret Squad",
        "Weapons": ["Ramming Speed"],
        "Traits": [],
    },
    "HornetMech": {
        "Name": "HornetMech",
        "Type": ["Brute", "Vek"],
        "Squad": "Secret Squad",
        "Weapons": ["Needle Shot"],
        "Traits": [],
    },
    "ScarabMech": {
        "Name": "ScarabMech",
        "Type": ["Ranged", "Vek"],
        "Squad": "Secret Squad",
        "Weapons": ["Explosive Goo"],
        "Traits": [],
    },

    # Bombermechs (Advanced Squad 1)
    "PierceMech": {
        "Name": "PierceMech",
        "Type": ["Brute"],
        "Squad": "Bombermechs",
        "Weapons": ["AP Cannon"],
        "Traits": [],
    },
    "BomblingMech": {
        "Name": "BomblingMech",
        "Type": ["Ranged"],
        "Squad": "Bombermechs",
        "Weapons": ["Bomb Dispenser"],
        "Traits": [],
    },
    "ExchangeMech": {
        "Name": "ExchangeMech",
        "Type": ["Science"],
        "Squad": "Bombermechs",
        "Weapons": ["Force Swap"],
        "Traits": [],
    },

    # Arachnophiles (Advanced Squad 2)
    "BulkMech": {
        "Name": "BulkMech",
        "Type": ["Prime"],
        "Squad": "Arachnophiles",
        "Weapons": ["Ricochet Rocket"],
        "Traits": [],
    },
    "ScorpioMech": {
        "Name": "ScorpioMech",
        "Type": ["Ranged"],
        "Squad": "Arachnophiles",
        "Weapons": ["Arachnoid Injector"],
        "Traits": [],
    },
    "FourwayMech": {
        "Name": "FourwayMech",
        "Type": ["Science"],
        "Squad": "Arachnophiles",
        "Weapons": ["Area Shift"],
        "Traits": [],
    },

    # Mist Eaters (Advanced Squad 3)
    "NeedleMech": {
        "Name": "NeedleMech",
        "Type": ["Prime"],
        "Squad": "Mist Eaters",
        "Weapons": ["Reverse Thrusters"],
        "Traits": ["Flying"],
    },
    "SmokeMech": {
        "Name": "SmokeMech",
        "Type": ["Ranged"],
        "Squad": "Mist Eaters",
        "Weapons": ["Smoldering Shells", "Nanofilter Mending"],
        "Traits": [],
    },
    "SupermanMech": {
        "Name": "SupermanMech",
        "Type": ["Science"],
        "Squad": "Mist Eaters",
        "Weapons": ["Control Shot"],
        "Traits": ["Flying"],
    },

    # Heat Sinkers (Advanced Squad 4)
    "InfernoMech": {
        "Name": "InfernoMech",
        "Type": ["Prime"],
        "Squad": "Heat Sinkers",
        "Weapons": ["Thermal Discharger"],
        "Traits": [],
    },
    "DoubletankMech": {
        "Name": "DoubletankMech",
        "Type": ["Brute"],
        "Squad": "Heat Sinkers",
        "Weapons": ["Quick-Fire Rockets"],
        "Traits": [],
    },
    "NapalmMech": {
        "Name": "NapalmMech",
        "Type": ["Science"],
        "Squad": "Heat Sinkers",
        "Weapons": ["Firestorm Generator", "Heat Engines"],
        "Traits": [],
    },

    # Cataclysm (Advanced Squad 5)
    "BottlecapMech": {
        "Name": "BottlecapMech",
        "Type": ["Prime"],
        "Squad": "Cataclysm",
        "Weapons": ["Hydraulic Lifter"],
        "Traits": [],
    },
    "TrimissileMech": {
        "Name": "TrimissileMech",
        "Type": ["Ranged"],
        "Squad": "Cataclysm",
        "Weapons": ["Tri-Rocket"],
        "Traits": [],
    },
    "HydrantMech": {
        "Name": "HydrantMech",
        "Type": ["Science"],
        "Squad": "Cataclysm",
        "Weapons": ["Seismic Capacitor"],
        "Traits": ["Flying"],
    },

    # Unimplemented Units
    "RockMech": {
        "Name": "RockMech",
        "Type": ["Prime"],
        "Squad": "Unimplemented",
        "Weapons": ["Rock Launcher"],
        "Traits": [],
    },
    "TinyheadMech": {  # It's BottlecapMech weaker
        "Name": "TinyheadMech",
        "Type": ["Prime"],
        "Squad": "Unimplemented",
        "Weapons": ["Hydraulic Lifter"],
        "Traits": [],
        "Disabled": True
    },
    "RocketcrabMech": {
        "Name": "RocketcrabMech",
        "Type": ["Brute"],
        "Squad": "Unimplemented",
        "Weapons": ["Guided Missile"],
        "Traits": [],
    },
    "TiltMech": {  # May be a bit OP with 4 damage/turn without any upgrade
        "Name": "TiltMech",
        "Type": ["Ranged"],
        "Squad": "Unimplemented",
        "Weapons": ["Rebounding Volley"],
        "Traits": [],
    },
    "NapalmMech2": {  # Same name as the science one, just less interesting
        "Name": "NapalmMech2",
        "Type": ["Ranged"],
        "Squad": "Unimplemented",
        "Weapons": ["Fire Beam", "Heat Engines"],
        "Traits": [],
        "Disabled": True
    },
    "PlacerMech": {  # Only deals one damage per mission, it's just bad
        "Name": "PlacerMech",
        "Type": ["Science"],
        "Squad": "Unimplemented",
        "Weapons": ["Grid Charger"],
        "Traits": ["Flying"],
        "Disabled": True
    },
}


def tags_from_unit(unit) -> dict[str, int]:
    tags = {}
    for weapon_name in unit["Weapons"]:
        weapon_tags = weapon_table[weapon_name]["Tags"]
        for tag in weapon_tags:
            cores = weapon_tags[tag]
            if tag not in tags or cores < tags[tag]:
                tags[tag] = cores

    for trait in unit["Traits"]:
        tags[trait] = 0

    return tags