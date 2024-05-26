from typing import Tuple, Optional, Callable
from BaseClasses import CollectionState
from ..Logic import unlocked_tags
from ..squad import Squad


class Achievement:
    def __init__(self, achievement_data: dict):
        self.squad = achievement_data["squad"]
        self.name = achievement_data["name"]
        self.required_tags: Optional[Tuple[str | Tuple[str]]] = achievement_data["required_tags"] if (
                "required_tags" in achievement_data) else None

    def is_doable_by_squad(self, squad: Squad) -> bool:
        return self.is_doable_by_tags(squad.get_tags())

    def get_access_rule(self, player: int) -> Callable[[CollectionState], bool]:
        return lambda state: self.is_doable_by_tags(unlocked_tags(state, player))

    def is_doable_by_tags(self, tags: set[str]) -> bool:
        if self.required_tags is None:
            return True
        for option in self.required_tags:
            if isinstance(option, str):
                if option in tags:
                    return True
            else:
                for required_part in option:
                    if required_part in tags:
                        break
                else:
                    return False
        return True
