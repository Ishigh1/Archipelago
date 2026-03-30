import dataclasses
from typing import Any, override

from BaseClasses import CollectionState
from Options import Option, Accessibility
from rule_builder.field_resolvers import FieldResolver, resolve_field, FromWorldAttr
from rule_builder.options import OptionFilter, Operator, OPERATORS
from rule_builder.rules import Rule, HasFromList, HasGroup, HasAll, False_, True_, Has, TWorld
from ..Constants import SEASON_CHAOTIC, SEASON_ITEMS, MARKET_LOCATIONS
from ...World import OracleOfSeasonsWorld
from ...Options import OracleOfSeasonsGoldenOreSpotsShuffle


@dataclasses.dataclass
class Bool(Rule[OracleOfSeasonsWorld], game=OracleOfSeasonsWorld.game):
    bool: FieldResolver
    value: Any
    operator: Operator

    def _instantiate(self, world: OracleOfSeasonsWorld) -> Rule.Resolved:
        if OPERATORS[self.operator](resolve_field(self.bool, world), self.value):
            return True_().resolve(world)
        else:
            return False_().resolve(world)


@dataclasses.dataclass
class LostWoods(HasAll, game=OracleOfSeasonsWorld.game):
    is_main_sequence: bool
    allow_default: bool

    def _instantiate(self, world: OracleOfSeasonsWorld) -> Rule.Resolved:
        if self.is_main_sequence:
            sequence = world.lost_woods_main_sequence
        else:
            sequence = world.lost_woods_item_sequence

        if self.allow_default:
            current_season = world.default_seasons["LOST_WOODS"]
        else:
            current_season = SEASON_CHAOTIC

        needed_seasons = set()
        for item in sequence:
            season = item[1]
            if season != current_season:
                current_season = SEASON_CHAOTIC
                needed_seasons.add(SEASON_ITEMS[season])

        self.item_names = tuple(needed_seasons)
        return super()._instantiate(world)


@dataclasses.dataclass
class ItemInLocation(Rule[OracleOfSeasonsWorld], game=OracleOfSeasonsWorld.game):
    location_name: str
    item_name: str

    @override
    def _instantiate(self, world: OracleOfSeasonsWorld) -> Rule.Resolved:
        if world.options.accessibility == Accessibility.option_full:
            return False_().resolve(world)
        return self.Resolved(
            self.location_name,
            self.item_name,
            player=world.player,
        )

    class Resolved(Rule.Resolved):
        location_name: str
        item_name: str

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            item = state.multiworld.get_location(self.location_name, self.player).item
            return item is not None and item.name == self.item_name and item.player == self.player

        @override
        def __str__(self) -> str:
            return f"{self.item_name} in {self.location_name}"


def from_bool(condition: bool) -> Rule:
    return True_() if condition else False_()


def from_option(option: type[Option], value: Any, operator: Operator = "eq") -> Rule:
    return True_(options=[OptionFilter(option, value, operator)])

def from_world_field(field: str, value: Any, operator: Operator = "eq") -> Rule:
    return Bool(FromWorldAttr(field), value, operator)