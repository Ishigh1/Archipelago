from worlds.minesweeper.game.board import Board


if __name__ == "__main__":
    board = Board(11, 20)
    board.generate_board(5, 5)
    board.display_ascii(True)