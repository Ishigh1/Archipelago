from dataclasses import dataclass

from Options import Toggle, Range, PerGameCommonOptions, StartInventoryPool


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
    display_name = "Required achievements%"
    range_start = 0
    range_end = 100
    default = 24


class SquadNumber(Range):
    """Number of squads included in the rando. Be careful to include at least as many as a third of required achievements"""
    display_name = "Squad number"
    range_start = 3
    range_end = 13
    default = 13


@dataclass
class IntoTheBreachOptions(PerGameCommonOptions):
    randomize_squads: RandomizeSquads
    custom_squad: CustomSquad
    required_achievements: RequiredAchievements
    squad_number: SquadNumber
    start_inventory_from_pool: StartInventoryPool
