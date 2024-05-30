import math
from typing import Tuple, Optional, Callable

from BaseClasses import CollectionState
from ..Logic import unlocked_tags, core_function


class Achievement:
    def __init__(self, achievement_data: dict):
        self.squad = achievement_data["squad"]
        self.name = achievement_data["name"]
        self.required_tags: Optional[Tuple[str | Tuple[str]]] = achievement_data["required_tags"] if (
                "required_tags" in achievement_data) else None

    def get_core_access_rule(self, world: "IntoTheBreachWorld", player: int) -> Callable[[CollectionState], bool]:
        tags = world.squads[self.squad].get_tags()
        _, rule = self.get_core_access_rule_with_tags(tags)
        if rule is None:
            return None
        else:
            return lambda state: rule(state, player)

    def get_custom_access_rule(self, player: int) -> Callable[[CollectionState], bool]:
        return lambda state: self.is_doable_by_tags(unlocked_tags(state, player), state, player)

    def get_core_access_rule_with_tags(self, tags: dict[str, int]) -> Tuple[bool, Callable[[CollectionState, int], bool]]:
        if self.required_tags is None:
            return True, None
        required_cores = 0
        for option in self.required_tags:
            option_cores = math.inf
            for required_part in option:
                if isinstance(required_part, str):
                    if required_part not in tags:
                        continue
                    required_part = tags[required_part]
                if required_part < option_cores:
                    option_cores = required_part
            if math.isinf(option_cores):
                return False, None
            if option_cores > required_cores:
                required_cores = option_cores
        if required_cores not in core_function:
            return True, None
        return True, core_function[required_cores]

    def is_doable_by_tags(self, tags: dict[str, int], state: CollectionState, player: int) -> bool:
        has_units, function = self.get_core_access_rule_with_tags(tags)
        return has_units and (function is None or function(state, player))
