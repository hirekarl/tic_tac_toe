"""Prompt players for moves."""

from typing import cast

from constants.constants import (
    PlayerMarker,
    CellKey,
    Cell,
    VALID_CELL_KEYS,
    CELL_KEY_TO_CELL_MAP,
)

from tic_tac_toe.models.board import Board, InvalidCellError, InvalidMoveError

from tic_tac_toe.utils.colorize import red, green, cyan


class InvalidCellKeyError(Exception):
    """Custom exception for when an incorrect cell key is provided."""

    _message: str

    def __init__(self, message: str = "Invalid cell key.") -> None:
        self._message: str = message
        super().__init__(self._message)


def _get_cell_from_cell_key(cell_key: CellKey) -> Cell:
    if not cell_key in VALID_CELL_KEYS:
        raise InvalidCellKeyError(f"Invalid cell key: {cell_key!r}.")

    cell: Cell = CELL_KEY_TO_CELL_MAP[cell_key]
    return cell


def prompt(player_marker: PlayerMarker, board: Board) -> None:
    """Prompt player `player_marker` for next move.

    Args:
        player_marker (PlayerMarker): "X" or "O".
        board (Board): The game board.
    """

    player_str = red("X") if player_marker == "X" else green("O")
    player_prompt: str = f"\n   {player_str} {cyan('→')} "

    while True:
        print(f"\n{board.stringify_board()}")
        move: str = input(player_prompt)

        try:
            cell = _get_cell_from_cell_key(cast(CellKey, move))
            board.make_move(cell, player_marker)
            break
        except (InvalidCellKeyError, InvalidCellError, InvalidMoveError) as _:
            print(red(" Try again "))
            continue
