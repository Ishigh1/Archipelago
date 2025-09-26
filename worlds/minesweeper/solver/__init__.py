from worlds.minesweeper.board.board import Board
from worlds.minesweeper.tile_hint import Number, TileHint, Bomb, NumberOrLess, NumberOrMore, INumberBetween


class Solver:
    def __init__(self, board: Board):
        self.board: Board = board

    def get_groups(self) -> dict[frozenset[int], TileHint]:
        groups = {}
        unknown_tiles = set()
        all_mines = Number(self.board.mines)
        for i in range(self.board.size ** 2):
            tile = self.board.get_tile(i)
            if tile is None:
                unknown_tiles.add(i)
                continue
            if isinstance(tile, Bomb):
                all_mines -= 1
                continue

            neighbor_tiles = set()
            for x, y in self.board.get_tiles_around(i):
                neighbor_tile = self.board.get_tile(x, y)
                if neighbor_tile is None:
                    neighbor_tiles.add(self.board.get_tile_index(x, y))
                elif isinstance(neighbor_tile, Bomb):
                    tile = tile - 1
            if len(neighbor_tiles) > 0:
                groups[frozenset(neighbor_tiles)] = tile
        if len(unknown_tiles) > 0:
            groups[frozenset(unknown_tiles)] = all_mines
        return groups

    def solve(self) -> bool:
        change = True
        while change:
            groups = self.get_groups()
            if len(groups) == 0:
                return True
            change = self.reveal_from_groups(groups)

            if change:
                continue

            hint_change = True
            depth = 0
            while not change and hint_change and depth < 3:
                depth += 1
                new_groups = self.deduce_from_groups(groups)
                change = self.reveal_from_groups(new_groups)

                hint_change = False
                if not change:
                    for position, group in new_groups.items():
                        if position not in groups:
                            groups[position] = group
                            hint_change = True
                        else:
                            old_hint = groups[position]
                            new_hint = groups[position] | group
                            if new_hint != old_hint:
                                hint_change = True
                                groups[position] |= group
                    if not hint_change:
                        break
        return False

    def reveal_from_groups(self, groups: dict[frozenset[int], TileHint]) -> bool:
        reveals_safe = set()
        reveals_bombs = set()
        for tiles, hint in groups.items():
            for tile in tiles:
                assert self.board.get_tile(tile) is None
            if isinstance(hint, NumberOrLess) and hint.value == 0:
                reveals_safe |= tiles
            elif isinstance(hint, NumberOrMore) and hint.value == len(tiles):
                reveals_bombs |= tiles

        tmp = False
        for tile in reveals_safe:
            self.board.reveal_safe(tile)
            tmp = True

        for tile in reveals_bombs:
            self.board.reveal_bomb(tile)
            tmp = True

        assert tmp == (len(reveals_safe) + len(reveals_bombs) > 0)
        return len(reveals_safe) + len(reveals_bombs) > 0

    def deduce_from_groups(self, groups: dict[frozenset[int], TileHint]) -> dict[frozenset[int], TileHint]:
        deductions = {}
        i = 0
        for tiles_1, mines_1 in groups.items():
            i += 1
            for tiles_2, mines_2 in groups.items():
                if tiles_1 == tiles_2:
                    continue

                intersection = tiles_1.intersection(tiles_2)
                if len(intersection) == 0:
                    continue

                if len(intersection) == len(tiles_2):
                    new_deduction = mines_1.remove_subset(mines_2)
                else:
                    new_deduction = mines_1.remove_union(mines_2)
                if new_deduction is None:
                    continue

                positions = frozenset(tiles_1.difference(intersection))
                for tile in positions:
                    assert self.board.get_tile(tile) is None

                assert isinstance(new_deduction, INumberBetween)
                if new_deduction.get_min_value() == 0 and new_deduction.get_max_value() >= len(positions):
                    continue

                if positions in deductions:
                    deductions[positions] |= new_deduction
                else:
                    deductions[positions] = new_deduction | NumberOrLess(len(positions))
        return deductions
