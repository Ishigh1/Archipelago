from Options import Option, Toggle
import typing


class RandomizeSquads(Toggle):
    """Randomize Squads"""
    display_name = "Randomize Squads"
    default = False


class CustomSquad(Toggle):
    """Only use the custom squad"""
    display_name = "Custom Squad Only"
    default = False


itb_options: typing.Dict[str, Option] = {
    "randomize_squads": RandomizeSquads,
    "custom_squad": CustomSquad
}
