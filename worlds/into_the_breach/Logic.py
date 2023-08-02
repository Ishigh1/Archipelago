from typing import Callable

from BaseClasses import CollectionState
from .Items import itb_island_items
from worlds.AutoWorld import LogicMixin
from .TagSystem import add_tags
from .Squads import squad_names


def can_get_achievement(achievement: str, player: int) -> Callable[[CollectionState], bool]:
    if achievement in ["Island Secure", "Overpowered", "Perfect Battle", "Lightning War", "Immortal"]:
        return lambda state: True
    if achievement in ["Watery Grave", "Unwitting Allies", "Pacifist"]:
        return lambda state: "Forced Move" in state.unlocked_tags(player)
    if achievement == "Ramming Speed":
        return lambda state: "Charge" in state.unlocked_tags(player)
    if achievement == "Stormy Weather":
        return lambda state: "Electric Smoke" in (l := state.unlocked_tags(player)) and "Smoke" in l
    if achievement == "Get Over Here":
        return lambda state: "Deadly Pull" in state.unlocked_tags(player)
    if achievement == "Glittering C-Beam":
        return lambda state: "Laser" in state.unlocked_tags(player)
    if achievement == "Shield Mastery":
        return lambda state: "Shield" in state.unlocked_tags(player)
    if achievement == "Chain Attack":
        return lambda state: "Chain" in state.unlocked_tags(player)
    if achievement == "Hold the Line":
        return lambda state: "Forced Move" in (l := state.unlocked_tags(player)) or "Summon" in l
    if achievement == "Unbreakable":
        return lambda state: "Armor" in state.unlocked_tags(player)
    if achievement == "Mass Displacement":
        return lambda state: "Triple Push" in state.unlocked_tags(player)
    if achievement == "Quantum Entanglement":
        return lambda state: "Teleport" in state.unlocked_tags(player)
    if achievement in ["Scorched Earth", "This is Fine"]:
        return lambda state: "Fire" in state.unlocked_tags(player)
    if achievement == "Cryo Expert":
        return lambda state: "Freeze" in state.unlocked_tags(player)
    if achievement == "Trick Shot":
        return lambda state: "Triple Kill" in state.unlocked_tags(player)
    if achievement == "Healing":
        return lambda state: "Heal" in (l := state.unlocked_tags(player)) or ("Smoke Heal" in l and "Smoke" in l)
    if achievement == "Overkill":
        return lambda state: ("Acid" in (l := state.unlocked_tags(player)) and (
                    "Hormones" in l or "Boost" in l or "High Damage" in l)) or ("Boost" in l and "High Damage" in l)
    raise Exception("Unexpected achievement : " + achievement)


class ItbLogic(LogicMixin):
    def count_if_in(self: [CollectionState], player: int, items: type([str])) -> int:
        return sum(self.has(item, player) for item in items)

    def has_islands(self, player: int, count: int) -> bool:
        return self.count_if_in(player, itb_island_items) >= count

    def has_defense(self: [CollectionState], player: int, count: int) -> bool:
        return self.item_count("3 Starting Grid Defense", player) * 3 >= count

    def has_starting_energy(self: [CollectionState], player: int, count: int) -> bool:
        return self.item_count("2 Starting Grid Power", player) * 2 + 1 >= count

    def can_beat_the_game(self, player: int) -> bool:
        return self.has_defense(player, 15) and self.has_starting_energy(player, 5)

    def unlocked_tags(self: [CollectionState], player: int) -> set[str]:
        tags = {}
        for squad_name in squad_names:
            if self.has(squad_name, player):
                add_tags(tags, self.multiworld.worlds[player].tags_by_squad[squad_name])

        return set(tags)
