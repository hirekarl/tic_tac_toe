"""Game board."""

from copy import deepcopy
from typing import Set, List, Tuple, Union, cast

from constants.constants import (
    PlayerMarker,
    CellValue,
    RowsCols,
    Cell,
    BOARD_SIZE,
    GRID_TOP,
    GRID_COL_JOINER,
    GRID_ROW_JOINER,
    GRID_BOTTOM,
)

from tic_tac_toe.utils.colorize import grey, red, green


class InvalidCellError(Exception):
    """Custom error for when an invalid cell is requested."""

    _message: str

    def __init__(self, message: str = "Invalid cell."):
        self._message: str = message
        super().__init__(self._message)


class InvalidMoveError(Exception):
    """Custom error for when an invalid move is attempted."""

    _message: str

    def __init__(self, message: str = "Invalid move."):
        self._message: str = message
        super().__init__(self._message)


BLANK_BOARD: List[List[CellValue]] = [
    [None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
]

VALID_MOVES: Set[PlayerMarker] = {"X", "O"}


class Board:
    """Game board."""

    _board: List[List[CellValue]]

    def __init__(
        self, starting_state: List[List[CellValue]] = deepcopy(BLANK_BOARD)
    ) -> None:
        self._board: List[List[CellValue]] = starting_state

    def __str__(self) -> str:
        return "Board"

    def __repr__(self) -> str:
        return "Board()"

    def _is_valid_cell(self, cell: Cell) -> bool:
        row, col = cell

        return 0 <= row <= BOARD_SIZE and 0 <= col <= BOARD_SIZE

    def _is_blank_cell(self, cell: Cell) -> bool:
        row, col = cell

        return self._board[row][col] is None

    def get_board(self) -> List[List[CellValue]]:
        """Get a copy of the game board state.

        Returns:
            List[List[CellValue]]: A copy of the game board state.
        """

        board_copy: List[List[CellValue]] = [row[:] for row in self._board]
        return board_copy

    def get_cell(self, cell: Cell) -> CellValue:
        """Get the value at (`row`, `col`) from the board.

        Args:
            cell (Cell): The tuple corresponding to the cell location on the board.
            move_value (MoveValue): "X" or "O".

        Raises:
            InvalidCellError: When an invalid (`row`, `col`) is requested.

        Returns:
            CellValue: The value ("X", "O", or `None`) at (`row`, `col`).
        """

        row, col = cell

        if not self._is_valid_cell(cell):
            raise InvalidCellError(f"({row}, {col}) is not a valid cell.")

        cell_value: CellValue = self._board[row][col]
        return cell_value

    def make_move(self, cell: Cell, move_value: PlayerMarker) -> None:
        """Play `move_value` ("X" or "O") at (`row`, `col`).

        Args:
            cell (Cell): The tuple corresponding to the cell location on the board.
                move_value (MoveValue): "X" or "O".

        Raises:
            InvalidCellError: When an attempt is made to play on an invalid cell.
            InvalidMoveError: When an attempt is made to play on a nonblank cell.
            InvalidMoveError: When an attempt is made to play a move other than "X" or "O".
        """

        row, col = cell

        if not self._is_valid_cell(cell):
            raise InvalidCellError(f"({row}, {col}) is not a valid cell.")

        if not self._is_blank_cell(cell):
            raise InvalidMoveError(
                f"{self._board[row][col]!r} already played at ({row}, {col})."
            )

        if not move_value in VALID_MOVES:
            raise InvalidMoveError(f"Invalid move: {move_value!r}.")

        self._board[row][col] = move_value

    def stringify_board(self) -> str:
        """Generate a string representation of the board.

        Raises:
            ValueError: If attempt is made to stringify a board of
                incorrect dimensions.
            ValueError: If the value of a cell is not "X", "O", or `None`.

        Returns:
            str: A stringified, colorized representation of the board.
        """

        rows: List[str] = []
        for row in range(BOARD_SIZE):
            cols: List[str] = []

            row = cast(RowsCols, row)
            for col in range(BOARD_SIZE):
                col = cast(RowsCols, col)

                value: CellValue = self.get_cell((row, col))
                cell_display: str = ""

                match value:
                    case None:
                        match row:
                            case 0:
                                cell_display = grey(f" {row + 7 + col} ")
                            case 1:
                                cell_display = grey(f" {row + 3 + col} ")
                            case 2:
                                cell_display = grey(f" {row - 1 + col} ")
                            case _:
                                raise ValueError(f"Invalid row index: {row!r}.")

                    case "X":
                        cell_display = red(" X ")
                    case "O":
                        cell_display = green(" O ")
                    case _:
                        raise ValueError(f"Invalid value: {value!r}.")

                cols.append(cell_display)

            row_display: str = GRID_COL_JOINER.join(cols)
            rows.append(row_display)

        board_display: str = f"{GRID_TOP}{GRID_ROW_JOINER.join(rows)}{GRID_BOTTOM}"
        return board_display

    def check_win(self) -> Tuple[bool, Union[PlayerMarker, None]]:
        """
        Checks the board for a win state.

        Returns:
            Tuple[bool, Union[MoveValue, None]]: A tuple where the boolean
                indicates if a win state exists (`True` or `False`), and the second element
                is the winning value ("X" or "O") if `True`, or `None` if `False`.
        """

        def _check_cell_values(
            a: CellValue, b: CellValue, c: CellValue
        ) -> Union[PlayerMarker, None]:
            if a is not None and a == b and b == c:
                return a
            return None

        for row in self._board:
            winner = _check_cell_values(row[0], row[1], row[2])
            if winner:
                return (True, winner)

        for col in range(BOARD_SIZE):
            winner = _check_cell_values(
                self._board[0][col], self._board[1][col], self._board[2][col]
            )
            if winner:
                return (True, winner)

        winner = _check_cell_values(
            self._board[0][0], self._board[1][1], self._board[2][2]
        )
        if winner:
            return (True, winner)

        winner = _check_cell_values(
            self._board[0][2], self._board[1][1], self._board[2][0]
        )
        if winner:
            return (True, winner)

        return (False, None)

    def check_draw(self) -> bool:
        """Checks the board for a draw state.

        Returns:
            bool: Whether the game is a draw (`True`) or not (`False`).
        """
        is_draw: bool = all(
            cell is not None for row in self._board for cell in row
        ) and self.check_win() == (False, None)

        return is_draw
