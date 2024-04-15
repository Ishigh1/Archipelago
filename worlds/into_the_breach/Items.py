from BaseClasses import Item


class ItbItem(Item):
    game = "Into The Breach"
    squad = False


itb_squad_items = [
    "Rusting Hulks",
    "Zenith Guard",
    "Blitzkrieg",
    "Steel Judoka",
    "Flame Behemoths",
    "Frozen Titans",
    "Hazardous Mechs",
    "Bombermechs",
    "Arachnophiles",
    # "Mist Eaters",
    # "Heat Sinkers",
    # "Cataclysm",
    # "Secret Squad",
    # "Random Squad",
    # "Custom Squad",
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

itb_progression_items = itb_squad_items + itb_island_items + itb_upgrade_items

itb_filler_items = [
    "1 Grid Power"
]
itb_trap_items = [
    # "-1 Grid Power", # Just a bad idea
    "Boss Enemy"
]
itb_items = itb_progression_items + itb_filler_items + itb_trap_items
