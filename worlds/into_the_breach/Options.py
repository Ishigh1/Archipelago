from Options import Option, Toggle
import typing


class RandomizeSquads(Toggle):
    """Randomize Squads
    Note that there is no logic"""
    display_name = "Randomize Squads"
    default = False


itb_options: typing.Dict[str, type(Option)] = {
    "randomize_squads": RandomizeSquads
}
