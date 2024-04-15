from Options import Option, Toggle, Range
import typing

from worlds.into_the_breach import itb_squad_items


class RandomizeSquads(Toggle):
    """Randomize Squads"""
    display_name = "Randomize Squads"
    default = False


class CustomSquad(Toggle):
    """Only use the custom squad"""
    display_name = "Custom Squad Only"
    default = False


class RequiredAchievements(Range):
    """Number of achievements required to win"""
    display_name = "Required achievements"
    range_start = 0
    range_end = (len(itb_squad_items) + 1)*3
    default = 9


itb_options: typing.Dict[str, type(Option)] = {
    "randomize_squads": RandomizeSquads,
    "custom_squad": CustomSquad,
    "required_achievements": RequiredAchievements
}
