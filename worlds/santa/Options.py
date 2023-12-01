import typing

from Options import AssembleOptions, Range


class LocationNumber(Range):
    """Number of different locations."""
    internal_name = "locations"
    default = 10
    range_start = 1
    range_end = 100
    display_name = "Number of different locations"

options: typing.Dict[str, AssembleOptions] = {
    "locations": LocationNumber
}