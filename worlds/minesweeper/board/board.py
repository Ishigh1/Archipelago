import random
from copy import deepcopy
from typing import Iterable

from worlds.minesweeper.tile_hint import TileHint, Number, Bomb


class Board:
    tiles: list[TileHint] | None = None  # Negative is bomb, other numbers are the value of the tile

    def __init__(self, size: int, mines: int):
        self.size: int = size
        self.mines: int = mines

    def get_tile_index(self, x: int, y: int = None) -> int:
        x, y = self.get_coords(x, y)
        return y * self.size + x

    def get_coords(self, x: int, y: int = None) -> tuple[int, int]:
        if y is None:
            y, x = divmod(x, self.size)
        return x, y

    def get_tiles_around(self, x: int, y: int = None) -> Iterable[tuple[int, int]]:
        x, y = self.get_coords(x, y)

        for i in range(max(0, x - 1), min(self.size, x + 2)):
            for j in range(max(0, y - 1), min(self.size, y + 2)):
                if i != x or j != y:
                    yield i, j

    def get_tile(self, x: int, y: int = None, force_revealed: bool = False) -> TileHint | None:
        tile = self.tiles[self.get_tile_index(x, y)]
        if not force_revealed and not tile.revealed:
            return None
        return tile

    def copy(self) -> "Board":
        new_board = Board(self.size, self.mines)
        new_board.tiles = deepcopy(self.tiles)
        return new_board

    def reveal_square(self, x: int, y: int = None):
        x, y = self.get_coords(x, y)
        if self.tiles is None:
            self.generate_board(x, y)
        tile = self.tiles[self.get_tile_index(x, y)]
        if tile.revealed:
            return
        tile.revealed = True
        if isinstance(tile, Number) and tile.value == 0:
            for i, j in self.get_tiles_around(x, y):
                self.reveal_square(i, j)

    def reveal_safe(self, x: int, y: int = None):
        self.reveal_square(x, y)
        if isinstance(self.get_tile(x, y), Bomb):
            raise Exception("Got a bomb")

    def reveal_bomb(self, x: int, y: int = None):
        self.reveal_square(x, y)
        if not isinstance(self.get_tile(x, y), Bomb):
            raise Exception("Got a non-bomb")

    def generate_board(self, x: int, y: int):
        valid_positions: list[int] = []
        for i in range(self.size):
            for j in range(self.size):
                if abs(i - x) > 1 or abs(j - y) > 1:
                    valid_positions.append(self.get_tile_index(i, j))

        mines = random.sample(valid_positions, self.mines)

        self.tiles = tiles = [Number(0)] * (self.size ** 2)

        for mine in mines:
            tiles[mine] = Bomb()
        for tile in range(self.size ** 2):
            if isinstance(tiles[tile], Bomb):
                continue
            bombs = 0
            for i, j in self.get_tiles_around(tile):
                if isinstance(self.get_tile(i, j, True), Bomb):
                    bombs += 1
            tiles[tile] = Number(bombs)

    def display_ascii(self, force_revealed: bool = False):
        for i in range(self.size):
            for j in range(self.size):
                tile = self.get_tile(i, j, force_revealed)
                if tile is None:
                    tile = "-"
                print(tile, end=" ")
            print()

    @classmethod
    def from_text(cls, text: str):
        lines = text.split("\n")
        board = Board(len(lines), text.count("X"))
        board.tiles = [Number(0)] * (board.size * board.size)

        i = 0
        for line in lines:
            for square in line.split(" "):
                if square == "":
                    continue
                if square == "X":
                    board.tiles[i] = Bomb()
                else:
                    board.tiles[i] = Number(int(square))
                i += 1
        return board
