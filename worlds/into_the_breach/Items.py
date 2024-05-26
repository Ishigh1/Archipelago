from BaseClasses import Item
from worlds.into_the_breach.squad.SquadInfo import squad_names


class ItbItem(Item):
    game = "Into The Breach"
    squad = False


itb_squad_items = squad_names

itb_upgrade_items = [
    "3 Starting Grid Defense",
    "2 Starting Grid Power",
]

itb_progression_items = itb_squad_items + itb_upgrade_items

itb_filler_items = [
    "1 Grid Power"
]
itb_trap_items = [
    # "-1 Grid Power", # Just a bad idea
    "Boss Enemy"
]
itb_items = itb_progression_items + itb_filler_items + itb_trap_items
