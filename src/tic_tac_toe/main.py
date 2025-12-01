"""CLI Tic-Tac-Toe."""

import sys

from tic_tac_toe.models.board import Board

from tic_tac_toe.game_loop import display_title, loop_game


def main() -> None:
    """Execute game."""

    board: Board = Board()

    display_title()
    loop_game(board)
    sys.exit(0)


if __name__ == "__main__":
    main()
