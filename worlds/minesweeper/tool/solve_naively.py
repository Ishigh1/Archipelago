import random

from worlds.minesweeper.board.board import Board
from worlds.minesweeper.solver import Solver
from worlds.minesweeper.tile_hint import Bomb


def naive_solve(board: Board):
    size = board.size
    changed = True

    while changed:
        changed = False

        for y in range(size):
            for x in range(size):
                number = board.get_tile(x, y)
                if number is None or isinstance(number, Bomb):
                    continue  # skip unrevealed or bombs

                number = number.value
                hidden_neighbors = []

                # Step 1: Find hidden neighbors
                for nx, ny in board.get_tiles_around(x, y):
                    tile = board.get_tile(nx, ny)
                    if tile is None:  # only unrevealed tiles
                        hidden_neighbors.append((nx, ny))
                    elif isinstance(tile, Bomb):
                        number -= 1

                # Step 2: If number of hidden neighbors equals the number → reveal them
                if len(hidden_neighbors) == number:
                    for nx, ny in hidden_neighbors:
                        board.reveal_bomb(nx, ny)
                        changed = True

                # Step 3: If number is 0 → reveal neighbors (like in reveal_square)
                if number == 0:
                    for nx, ny in board.get_tiles_around(x, y):
                        if board.get_tile(nx, ny) is None:
                            board.reveal_safe(nx, ny)
                            changed = True


if __name__ == "__main__":
    seed = random.getrandbits(128)
    seed = 291207997407765524087505877399389412672
    random.seed(seed)
    while True:
        print(seed)
        random.seed(seed)
        board = Board(21, 50)
        board.reveal_safe(10, 10)
        if Solver(board).solve():
            pass
            # break
        else:
            board.display_ascii()
        seed = random.getrandbits(128)
    print()
    board.display_ascii()

    print()

    board.display_ascii(True)