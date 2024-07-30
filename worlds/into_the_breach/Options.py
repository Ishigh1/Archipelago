from dataclasses import dataclass

from schema import Schema, Or, Optional

from Options import Toggle, Range, PerGameCommonOptions, StartInventoryPool, OptionDict, Choice
from worlds.into_the_breach.squad.SquadInfo import squad_names
from worlds.into_the_breach.squad.Units import unit_table


class RandomizeSquads(Toggle):
    """Randomize Squads"""
    display_name = "Randomize Squads"
    default = True


class CustomSquad(Toggle):
    """Only use the custom squad"""
    display_name = "Custom Squad Only"
    default = False


class RequiredAchievements(Range):
    """Percentage of achievements required to win"""
    display_name = "Required achievements"
    range_start = 0
    range_end = 100
    default = 24


class Difficulty(Choice):
    """Required difficulty to beat the game"""
    display_name = "Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_unfair = 3
    default = option_easy


class SquadNumber(Range):
    """Number of squads included in the rando."""
    display_name = "Squad number"
    range_start = 3
    range_end = 13
    default = range_end


class UnitPlando(OptionDict):
    """If you want some units in some squads, use the form unit "name: squad name"."""
    value: dict[str, str]
    valid_keys = frozenset(unit_table)
    schema = Schema({
        Optional(Or(*unit_table)): Or(*squad_names)
    })


@dataclass
class IntoTheBreachOptions(PerGameCommonOptions):
    randomize_squads: RandomizeSquads
    custom_squad: CustomSquad
    required_achievements: RequiredAchievements
    difficulty: Difficulty
    squad_number: SquadNumber
    start_inventory_from_pool: StartInventoryPool
    unit_plando: UnitPlando
