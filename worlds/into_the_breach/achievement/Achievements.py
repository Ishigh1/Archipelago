from . import Achievement

achievement_info_table = {
    # "achievement name": {
    #   "squad": "squad name",
    #   "name": "achievement name,
    #   "description": "Whatever",
    #   "required_tags: (mandatory_option1, (option_for_mandatory_option_2, option_for_mandatory_option_2))
    # },
    "Watery Grave": {
        "squad": "Rift Walkers",
        "name": "Watery Grave",
        "description": "Drown 3 enemies in water in a single battle with the Rift Walkers squad",
        "required_tags": (("Forced Move",),)
    },
    "Ramming Speed": {
        "squad": "Rift Walkers",
        "name": "Ramming Speed",
        "description": "Kill an enemy 5 or more tiles away with a Dash Punch with the Rift Walkers squad",
        "required_tags": (("Charge",),)
    },
    "Island Secure": {
        "squad": "Rift Walkers",
        "name": "Island Secure",
        "description": "Complete 1st Corporate Island with the Rift Walkers squad",
        "required_tags": None
    },
    "Overpowered": {
        "squad": "Rusting Hulks",
        "name": "Overpowered",
        "description": "Overpower your Power Grid twice by earning or buying Power when it is full with the Rusting Hulks squad",
        "required_tags": ((1,),)
    },
    "Stormy Weather": {
        "squad": "Rusting Hulks",
        "name": "Stormy Weather",
        "description": "Deal 12 damage with Electric Smoke in a single battle with the Rusting Hulks squad",
        "required_tags": (("Electric Smoke 2",), ("Smoke",))
    },
    "Perfect Battle": {
        "squad": "Rusting Hulks",
        "name": "Perfect Battle",
        "description": "Take no Mech or Building Damage in a single battle with the Rusting Hulks squad (Repaired damage is still damage)",
        "required_tags": None
    },
    "Get Over Here": {
        "squad": "Zenith Guard",
        "name": "Get Over Here",
        "description": "Kill an enemy by pulling it into yourself with the Zenith Guard squad",
        "required_tags": (("Deadly Pull",),)
    },
    "Glittering C-Beam": {
        "squad": "Zenith Guard",
        "name": "Glittering C-Beam",
        "description": "Hit 4 enemies with a single laser with the Zenith Guard squad",
        "required_tags": (("Laser",),)
    },
    "Shield Mastery": {
        "squad": "Zenith Guard",
        "name": "Shield Mastery",
        "description": "Block damage with a Shield 4 times in a single battle with the Zenith Guard squad",
        "required_tags": (("Shield",),)
    },
    "Chain Attack": {
        "squad": "Blitzkrieg",
        "name": "Chain Attack",
        "description": "Have the Chain Whip attack chain through 10 tiles with the Blitzkrieg squad",
        "required_tags": (("Chain",),)
    },
    "Lightning War": {
        "squad": "Blitzkrieg",
        "name": "Lightning War",
        "description": "Finish the first 2 Corporate Islands in under 30 minutes with the Blitzkrieg squad",
        "required_tags": ((3,),)
    },
    "Hold the Line": {
        "squad": "Blitzkrieg",
        "name": "Hold the Line",
        "description": "Block 4 emerging Vek in a single turn with the Blitzkrieg squad",
        "required_tags": (("Forced Move", "Summon"),)
    },
    "Unbreakable": {
        "squad": "Steel Judoka",
        "name": "Unbreakable",
        "description": "Have Mech Armor absorb 5 damage in a single battle with the Steel Judoka squad",
        "required_tags": (("Armor",),)
    },
    "Unwitting Allies": {
        "squad": "Steel Judoka",
        "name": "Unwitting Allies",
        "description": "Have 4 enemies die from enemy fire in a single battle with the Steel Judoka squad",
        "required_tags": (("Forced Move",), (1,))
    },
    "Mass Displacement": {
        "squad": "Steel Judoka",
        "name": "Mass Displacement",
        "description": "Push 3 enemies with a single attack with the Steel Judoka squad",
        "required_tags": (("Triple Push",), (1,))
    },
    "Quantum Entanglement": {
        "squad": "Flame Behemoths",
        "name": "Quantum Entanglement",
        "description": "Teleport a unit 4 tiles away with the Flame Behemoths squad",
        "required_tags": (("Teleport",),)
    },
    "Scorched Earth": {
        "squad": "Flame Behemoths",
        "name": "Scorched Earth",
        "description": "End a battle with 12 tiles on Fire with the Flame Behemoths squad",
        "required_tags": (("Fire",), (1,))
    },
    "This is Fine": {
        "squad": "Flame Behemoths",
        "name": "This is Fine",
        "description": "Have 5 enemies on Fire simultaneously with the Flame Behemoths squad",
        "required_tags": (("Fire",), (2,))
    },
    "Cryo Expert": {
        "squad": "Frozen Titans",
        "name": "Cryo Expert",
        "description": "Shoot the Cryo-Launcher 4 times in a single battle with the Frozen Titans squad",
        "required_tags": (("Freeze",),)
    },
    "Pacifist": {
        "squad": "Frozen Titans",
        "name": "Pacifist",
        "description": "Kill less than 3 enemies in a single battle with the Frozen Titans squad",
        "required_tags": (("Forced Move",),)
    },
    "Trick Shot": {
        "squad": "Frozen Titans",
        "name": "Trick Shot",
        "description": "Kill 3 enemies with a single attack of the Janus Cannon with the Frozen Titans squad",
        "required_tags": (("Triple Kill",),)
    },
    "Healing": {
        "squad": "Hazardous Mechs",
        "name": "Healing",
        "description": "Heal 10 Mech Health in a single battle with the Hazardous Mechs squad",
        "required_tags": (("Heal",),)
    },
    "Immortal": {
        "squad": "Hazardous Mechs",
        "name": "Immortal",
        "description": "Finish 4 Corporate Islands without a Mech being destroyed at the end of a battle with the Hazardous Mechs squad",
        "required_tags": ((5,),)
    },
    "Overkill": {
        "squad": "Hazardous Mechs",
        "name": "Overkill",
        "description": "Deal 8 damage to a unit with a single attack with the Hazardous Mechs squad",
        "required_tags": (("Acid", "Hormones"), (2,))
    },
    "Change the Odds": {
        "squad": "Random Squad",
        "name": "Change the Odds",
        "description": "Raise Grid Defense to 30% or more with a Random squad",
    },
    "Loot Boxes!": {
        "squad": "Random Squad",
        "name": "Loot Boxes!",
        "description": "Open 5 Time Pods in a single game with a Random squad",
    },
    "Lucky Start": {
        "squad": "Random Squad",
        "name": "Lucky Start",
        "description": "Beat the game (any length) without spending any Reputation with a Random squad",
    },
    "Class Specialist": {
        "squad": "Custom Squad",
        "name": "Class Specialist",
        "description": "Beat the game with 3 different Mechs from the same class in a Custom squad",
    },
    "Flight Specialist": {
        "squad": "Custom Squad",
        "name": "Flight Specialist",
        "description": "Beat the game with 3 flying Mechs in a Custom squad",
    },
    "Mech Specialist": {
        "squad": "Custom Squad",
        "name": "Mech Specialist",
        "description": "Beat the game with 3 of the same Mech in a Custom squad",
    },
    "Hold the Door": {
        "squad": "Bombermechs",
        "name": "Hold the Door",
        "description": "Block 30 Emerging Vek enemies by the end of Island 2",
        "required_tags": ((2,),),
    },
    "No Survivors": {
        "squad": "Bombermechs",
        "name": "No Survivors",
        "description": "Have 7 units (any team) die in a single turn",
        "required_tags": (("Triple Kill", "Hoard Summon"), (2,))
    },
    "Powered Blast": {
        "squad": "Bombermechs",
        "name": "Powered Blast",
        "description": "Pierce a Walking Bomb with the AP Cannon to kill an Enemy",
        "required_tags": (("Summon",), ("Piercing",),)
    },
    "Spider Breeding": {
        "squad": "Arachnophiles",
        "name": "Spider Breeding",
        "description": "Spawn 15 Arachnoids in one Island",
        "required_tags": (("Many Summons",),)
    },
    "Working Together": {
        "squad": "Arachnophiles",
        "name": "Working Together",
        "description": "Area Shift 4 units at once",
        "required_tags": (("Quadruple Move",), (1,))
    },
    "Efficient Explosives": {
        "squad": "Arachnophiles",
        "name": "Efficient Explosives",
        "description": "Kill 3 Enemies with 1 shot of the Ricochet Rocket",
        "required_tags": (("Triple Kill",),)
    },
    "Stay With Me!": {
        "squad": "Mist Eaters",
        "name": "Stay With Me!",
        "description": "Heal 12 damage over the course of a single Island",
        "required_tags": (("Heal",),)
    },
    "Let's Walk": {
        "squad": "Mist Eaters",
        "name": "Let's Walk",
        "description": "Move Enemies with Control Shot 120 spaces in one game",
        "required_tags": (("Forced Move",), (3,))
    },
    "On the Backburner": {
        "squad": "Mist Eaters",
        "name": "On the Backburner",
        "description": "Do 4 damage with the Reverse Thrusters",
        "required_tags": (("High Damage",),)
    },
    "Boosted": {
        "squad": "Heat Sinkers",
        "name": "Boosted",
        "description": "Boost 8 Mechs in one mission",
        "required_tags": (("Boost",), (1,))
    },
    "Feed the Flame": {
        "squad": "Heat Sinkers",
        "name": "Feed the Flame",
        "description": "Light 3 Enemies on fire with a single attack",
        "required_tags": (("Triple Fire",),)
    },
    "Maximum Firepower": {
        "squad": "Heat Sinkers",
        "name": "Maximum Firepower",
        "description": "Deal 8 damage with a single activation of the Quick-Fire Rockets",
        "required_tags": (("High Damage", "Acid"),
                          ("Triple Kill", "Acid"),
                          ("High Damage", "Triple Kill"))
    },
    "Unstable Ground": {
        "squad": "Cataclysm",
        "name": "Unstable Ground",
        "description": "Crack 10 tiles in one mission",
        "required_tags": (("Crack",),)
    },
    "Core of the Earth": {
        "squad": "Cataclysm",
        "name": "Core of the Earth",
        "description": "Drop 10 Enemies into pits on one Island",
        "required_tags": (("Crack",), ("Forced Move",), (1,))
    },
    "Miner Inconvenience": {
        "squad": "Cataclysm",
        "name": "Miner Inconvenience",
        "description": "Destroy 20 mountains in one game",
        "required_tags": ((2,),)
    }
}

achievement_table: dict[str, Achievement] = {key: Achievement(value) for key, value in achievement_info_table.items()}

# Group items by squad
achievements_by_squad: dict[str, dict[str, Achievement]] = {}
for key, data in achievement_table.items():
    squad = data.squad
    if squad in achievements_by_squad:
        achievements_by_squad[squad][key] = data
    else:
        achievements_by_squad[squad] = {key: data}
