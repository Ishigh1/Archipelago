from BaseClasses import Item


class MyGameItem(Item):
    game = "Into The Breach"


itb_unlock_items = [
    "Unlock Rusting Hulks",
    "Unlock Zenith Guard",
    "Unlock Blitzkrieg",
    "Unlock Steel Judoka",
    "Unlock Flame Behemoths",
    "Unlock Frozen Titans",
    "Unlock Hazardous Mechs",
    # "Unlock Bombermechs",
    # "Unlock Arachnophiles",
    # "Unlock Mist Eaters",
    # "Unlock Heat Sinkers",
    # "Unlock Cataclysm",
    # "Unlock Random Squad",
    # "Unlock Custom Squad",
]

itb_island_items = [  # Not implemented yet
    # "Unlock Museum Island",
    # "Unlock Desert Island",
    # "Unlock Ice Island",
    # "Unlock Factory Island",
    # "Unlock Hive"
]

itb_upgrade_items = [
    "3 Starting Grid Defense",
    "2 Starting Grid Power",
]

itb_progression_items = itb_unlock_items + itb_island_items + itb_upgrade_items

itb_filler_items = [
    "1 Grid Power"
]
itb_trap_items = [
    "-1 Grid Power"
]
itb_items = itb_progression_items + itb_filler_items + itb_trap_items
