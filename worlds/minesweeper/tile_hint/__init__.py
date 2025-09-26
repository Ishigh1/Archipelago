import math
from typing import Union


class TileHint:
    def __init__(self):
        self.revealed = False

    def __str__(self):
        return self.str_code()

    def str_code(self) -> str:
        raise NotImplementedError()

    def __or__(self, other: "TileHint") -> "TileHint":
        return Or(self, other)

    def remove_subset(self, tilehint: "TileHint") -> Union["TileHint", None]:
        return self.remove_union(tilehint)

    def remove_union(self, tilehint: "TileHint") -> Union["TileHint", None]:
        return None


class Bomb(TileHint):
    def str_code(self) -> str:
        return "X"


class Or(TileHint):
    def str_code(self) -> str:
        return f"{self.sub_hint1}|{self.sub_hint2}"

    def __init__(self, sub_hint1: TileHint, sub_hint2: TileHint):
        self.sub_hint1 = sub_hint1
        self.sub_hint2 = sub_hint2

    def __or__(self, other: TileHint) -> TileHint:
        return self.sub_hint1 | (self.sub_hint2 | other)


def simplify_between(min_value, max_value) -> TileHint:
    if min_value == max_value:
        return Number(min_value)
    elif min_value <= 0:
        return NumberOrLess(max_value)
    elif max_value == math.inf:
        return NumberOrMore(min_value)
    else:
        return NumberBetween(min_value, max_value)


class INumberBetween(TileHint):
    def get_min_value(self) -> int:
        return 0

    def get_max_value(self) -> int:
        return math.inf

    def remove_subset(self, tilehint: TileHint) -> Union[TileHint, None]:
        if not isinstance(tilehint, INumberBetween):
            return super().remove_subset(tilehint)

        min_value = self.get_min_value() - tilehint.get_max_value()
        max_value = self.get_max_value() - tilehint.get_min_value()
        return simplify_between(min_value, max_value)

    def remove_union(self, tilehint: TileHint) -> Union[TileHint, None]:
        if not isinstance(tilehint, INumberBetween):
            return super().remove_union(tilehint)

        min_value = self.get_min_value() - tilehint.get_max_value()
        return simplify_between(min_value, self.get_max_value())

    def __or__(self, other: TileHint) -> TileHint:
        if not isinstance(other, INumberBetween):
            return super.__or__(other)
        min_value = max(self.get_min_value(), other.get_min_value())
        max_value = min(self.get_max_value(), other.get_max_value())

        return simplify_between(min_value, max_value)

    def __eq__(self, other: TileHint) -> bool:
        if not isinstance(other, INumberBetween):
            return super().__eq__(other)
        return self.get_min_value() == other.get_min_value() and self.get_max_value() == other.get_max_value()


class NumberBetween(INumberBetween):
    def __init__(self, min_value: int, max_value: int):
        self.min = min_value
        self.max = max_value

    def str_code(self) -> str:
        return f"{self.min}-{self.max}"

    def get_min_value(self) -> int:
        return self.min

    def get_max_value(self) -> int:
        return self.max


class NumberedHint(TileHint):
    def __init__(self, value: int):
        assert isinstance(value, int)
        self.value = value
        super().__init__()

    def __sub__(self, other: object) -> "NumberedHint":
        if isinstance(other, int):
            return self.__class__(self.value - other)
        raise TypeError()


class NumberOrMore(NumberedHint, INumberBetween):
    def str_code(self) -> str:
        return f"{self.value}+"

    def get_min_value(self) -> int:
        return self.value


class NumberOrLess(NumberedHint, INumberBetween):
    def str_code(self) -> str:
        return f"{self.value}-"

    def get_max_value(self) -> int:
        return self.value


class Number(NumberOrMore, NumberOrLess):
    def str_code(self) -> str:
        return str(self.value)

    def __or__(self, other: TileHint) -> TileHint:
        return self
