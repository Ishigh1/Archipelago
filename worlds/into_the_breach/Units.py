# This file will list all the units, their categories, and their weapons

unit_list = {
    # Rift Walkers (Squad Archive A)
    "PunchMech": {
        "Type": ["Prime"],
        "Squad": "Rift Walkers",
        "Weapons": ["Titan Fist"],
        "Traits": [],
    },
    "TankMech": {
        "Type": ["Brute"],
        "Squad": "Rift Walkers",
        "Weapons": ["Taurus Cannon"],
        "Traits": [],
    },
    "ArtiMech": {
        "Type": ["Ranged"],
        "Squad": "Rift Walkers",
        "Weapons": ["Artemis Artillery"],
        "Traits": [],
    },

    # Rusting Hulks (Squad Rust A)
    "JetMech": {
        "Type": ["Brute"],
        "Squad": "Rusting Hulks",
        "Weapons": ["Aerial Bombs"],
        "Traits": ["Flying"],
    },
    "RocketMech": {
        "Type": ["Ranged"],
        "Squad": "Rusting Hulks",
        "Weapons": ["Rocket Artillery", "Storm Generator"],
        "Traits": [],
    },
    "PulseMech": {
        "Type": ["Science"],
        "Squad": "Rusting Hulks",
        "Weapons": ["Repulse"],
        "Traits": [],
    },

    # Zenith Guard (Squad Pinnacle A)
    "LaserMech": {
        "Type": ["Prime"],
        "Squad": "Zenith Guard",
        "Weapons": ["Burst Beam"],
        "Traits": [],
    },
    "ChargeMech": {
        "Type": ["Brute"],
        "Squad": "Zenith Guard",
        "Weapons": ["Ramming Engines"],
        "Traits": [],
    },
    "ScienceMech": {
        "Type": ["Science"],
        "Squad": "Zenith Guard",
        "Weapons": ["Attraction Pulse", "Shield Projector"],
        "Traits": ["Flying"],
    },

    # Blitzkrieg (Squad Detritus A)
    "ElectricMech": {
        "Type": ["Prime"],
        "Squad": "Blitzkrieg",
        "Weapons": ["Electric Whip"],
        "Traits": [],
    },
    "WallMech": {
        "Type": ["Brute"],
        "Squad": "Blitzkrieg",
        "Weapons": ["Grappling Hook"],
        "Traits": ["Armor"],
    },
    "RockartMech": {
        "Type": ["Ranged"],
        "Squad": "Blitzkrieg",
        "Weapons": ["Rock Accelerator"],
        "Traits": [],
    },

    # Steel Judoka (Squad Archive B)
    "JudoMech": {
        "Type": ["Prime"],
        "Squad": "Steel Judoka",
        "Weapons": ["Vice Fist"],
        "Traits": ["Armor"],
    },
    "DStrikeMech": {
        "Type": ["Ranged"],
        "Squad": "Steel Judoka",
        "Weapons": ["Cluster Artillery"],
        "Traits": [],
    },
    "GravMech": {
        "Type": ["Science"],
        "Squad": "Steel Judoka",
        "Weapons": ["Grav Well", "Vek Hormones"],
        "Traits": [],
    },

    # Flame Behemoths (Squad Rust B)
    "FlameMech": {
        "Type": ["Prime"],
        "Squad": "Flame Behemoths",
        "Weapons": ["Flame Thrower"],
        "Traits": [],
    },
    "IgniteMech": {
        "Type": ["Ranged"],
        "Squad": "Flame Behemoths",
        "Weapons": ["Vulcan Artillery"],
        "Traits": [],
    },
    "TeleMech": {
        "Type": ["Science"],
        "Squad": "Flame Behemoths",
        "Weapons": ["Teleporter"],
        "Traits": [],
    },

    # Frozen Titans (Squad Pinnacle B)
    "GuardMech": {
        "Type": ["Prime"],
        "Squad": "Frozen Titans",
        "Weapons": ["Spartan Shield"],
        "Traits": [],
    },
    "MirrorMech": {
        "Type": ["Brute"],
        "Squad": "Frozen Titans",
        "Weapons": ["Janus Cannon"],
        "Traits": [],
    },
    "IceMech": {
        "Type": ["Ranged"],
        "Squad": "Frozen Titans",
        "Weapons": ["Cryo-Launcher"],
        "Traits": ["Flying"],
    },

    # Hazardous Mechs (Squad Detritus B)
    "LeapMech": {
        "Type": ["Prime"],
        "Squad": "Hazardous Mechs",
        "Weapons": ["Hydraulic Legs"],
        "Traits": [],
    },
    "UnstableTank": {
        "Type": ["Brute"],
        "Squad": "Hazardous Mechs",
        "Weapons": ["Unstable Cannon"],
        "Traits": [],
    },
    "NanoMech": {
        "Type": ["Science"],
        "Squad": "Hazardous Mechs",
        "Weapons": ["A.C.I.D Projector", "Viscera Nanobots"],
        "Traits": ["Flying"],
    },

    # Secret Squad
    "BeetleMech": {
        "Type": ["Prime", "Vek"],
        "Squad": "Secret Squad",
        "Weapons": ["Ramming speed"],
        "Traits": [],
    },
    "HornetMech": {
        "Type": ["Brute", "Vek"],
        "Squad": "Secret Squad",
        "Weapons": ["Needle Shot"],
        "Traits": [],
    },
    "ScarabMech": {
        "Type": ["Ranged", "Vek"],
        "Squad": "Secret Squad",
        "Weapons": ["Explosive Goo"],
        "Traits": [],
    },

    # Bombermechs (Advanced Squad 1)
    "PierceMech": {
        "Type": ["Brute"],
        "Squad": "Bombermechs",
        "Weapons": ["AP Cannon"],
        "Traits": [],
    },
    "BomblingMech": {
        "Type": ["Ranged"],
        "Squad": "Bombermechs",
        "Weapons": ["Bomb Dispenser"],
        "Traits": [],
    },
    "ExchangeMech": {
        "Type": ["Science"],
        "Squad": "Bombermechs",
        "Weapons": ["Force Swap"],
        "Traits": [],
    },

    # Arachnophiles (Advanced Squad 2)
    "BulkMech": {
        "Type": ["Prime"],
        "Squad": "Arachnophiles",
        "Weapons": ["Ricochet Rocket"],
        "Traits": [],
    },
    "ScorpioMech": {
        "Type": ["Ranged"],
        "Squad": "Arachnophiles",
        "Weapons": ["Arachnoid Injector"],
        "Traits": [],
    },
    "FourwayMech": {
        "Type": ["Science"],
        "Squad": "Arachnophiles",
        "Weapons": ["Area Shift"],
        "Traits": [],
    },

    # Mist Eaters (Advanced Squad 3)
    "NeedleMech": {
        "Type": ["Prime"],
        "Squad": "Mist Eaters",
        "Weapons": ["Reverse Thrusters"],
        "Traits": ["Flying"],
    },
    "SmokeMech": {
        "Type": ["Ranged"],
        "Squad": "Mist Eaters",
        "Weapons": ["Smoldering Shells", "Nanofilter Mending"],
        "Traits": [],
    },
    "SupermanMech": {
        "Type": ["Science"],
        "Squad": "Mist Eaters",
        "Weapons": ["Control Shot"],
        "Traits": ["Flying"],
    },

    # Heat Sinkers (Advanced Squad 4)
    "InfernoMech": {
        "Type": ["Prime"],
        "Squad": "Heat Sinkers",
        "Weapons": ["Thermal Discharger"],
        "Traits": [],
    },
    "DoubletankMech": {
        "Type": ["Brute"],
        "Squad": "Heat Sinkers",
        "Weapons": ["Quick-Fire Rockets"],
        "Traits": [],
    },
    "NapalmMech": {
        "Type": ["Science"],
        "Squad": "Heat Sinkers",
        "Weapons": ["Firestorm Generator", "Heeat Engines"],
        "Traits": [],
    },

    # Cataclysm (Advanced Squad 5)
    "BottlecapMech": {
        "Type": ["Prime"],
        "Squad": "Cataclysm",
        "Weapons": ["Hydraulic Lifter"],
        "Traits": [],
    },
    "TrimissileMech": {
        "Type": ["Ranged"],
        "Squad": "Cataclysm",
        "Weapons": ["Tri-Rocket"],
        "Traits": [],
    },
    "HydrantMech": {
        "Type": ["Science"],
        "Squad": "Cataclysm",
        "Weapons": ["Seismic Capacitor"],
        "Traits": ["Flying"],
    },

    # Unimplemented Units
    "RockMech": {
        "Type": ["Prime"],
        "Squad": "Unimplemented",
        "Weapons": ["Rock Launcher"],
        "Traits": [],
    },
    "TinyheadMech": {  # It's BottlecapMech weaker
        "Type": ["Prime"],
        "Squad": "Unimplemented",
        "Weapons": ["Hydraulic Lifter"],
        "Traits": [],
        "Disabled": True
    },
    "RocketcrabMech": {
        "Type": ["Brute"],
        "Squad": "Unimplemented",
        "Weapons": ["Guided Missile"],
        "Traits": [],
    },
    "TiltMech": {  # May be a bit OP with 4 damage/turn without any upgrade
        "Type": ["Ranged"],
        "Squad": "Unimplemented",
        "Weapons": ["Rebounding Volley"],
        "Traits": [],
    },
    "NapalmMech2": {  # Same name as the science one, just less interesting
        "Type": ["Ranged"],
        "Squad": "Unimplemented",
        "Weapons": ["Fire Beam", "Heat Engines"],
        "Traits": [],
        "Disabled": True
    },
    "PlacerMech": {  # Only deals one damage per mission, it's just bad
        "Type": ["Science"],
        "Squad": "Unimplemented",
        "Weapons": ["Grid Charger"],
        "Traits": ["Flying"],
        "Disabled": True
    },
}
