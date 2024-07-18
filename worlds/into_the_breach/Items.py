from BaseClasses import Item
from worlds.into_the_breach.squad.SquadInfo import squad_names


class ItbItem(Item):
    game = "Into The Breach"
    squad = False
    start_power = 0


itb_squad_items = squad_names

itb_upgrade_items = [
    "3 Starting Grid Defense",
    "2 Starting Grid Power",
    "1 Starting Grid Power",
    "1 Starting Power Core",
]

itb_progression_items = itb_squad_items + itb_upgrade_items

itb_filler_items = [
    "3 Grid Power",
    "2 Power Cores"
]

itb_common_trap_items = [
    "Airstrike Trap",
    "Boulder Trap",
    "Lightning Trap",
    "Snowstorm Trap",
    "Wind Trap",
    "Landfall Trap"
]

itb_uncommon_trap_items = [
    "Boss Enemy Trap",
]

itb_legendary_trap_items = [
    "All Trap"
]

itb_trap_items = itb_common_trap_items + itb_uncommon_trap_items + itb_legendary_trap_items

itb_items = itb_progression_items + itb_filler_items + itb_trap_items
