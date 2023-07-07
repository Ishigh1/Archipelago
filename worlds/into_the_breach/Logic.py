from .Items import itb_island_items
from worlds.AutoWorld import LogicMixin


def count_if_in(state, player, items: type([str])) -> int:
    return sum(state.has(item, player) for item in items)


class ItbLogic(LogicMixin):
    def has_islands(self, player: int, count: int) -> bool:
        return count_if_in(self, player, itb_island_items) >= count

    def has_defense(self, player: int, count: int) -> bool:
        return self.item_count("3 Starting Grid Defense", player) * 3 >= count

    def has_starting_energy(self, player: int, count: int) -> bool:
        return self.item_count("2 Starting Grid Power", player) * 2 + 1 >= count

    def can_beat_the_game(self, player: int) -> bool:
        return self.has_defense(player, 15) and self.has_starting_energy(player, 5)
