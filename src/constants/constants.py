"""Game constants."""

from typing import Literal, Mapping, Set, Tuple, Union

# Types
type PlayerMarker = Literal["X", "O"]
type CellValue = Union[PlayerMarker, None]
type CellKey = Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
type RowsCols = Literal[0, 1, 2]
type Cell = Tuple[RowsCols, RowsCols]

# Game Setup
BOARD_SIZE: int = 3  # NB: Do not change! Board size should *only* ever be 3.

# ANSI Escape Sequences
ANSI_GREY: str = "\033[90m"
ANSI_RED: str = "\033[31m"
ANSI_GREEN: str = "\033[32m"
ANSI_YELLOW: str = "\033[33m"
ANSI_MAGENTA: str = "\033[35m"
ANSI_CYAN: str = "\033[36m"
ANSI_RESET: str = "\033[0m"

# Board Grid Components
GRID_TOP: str = "   ╻   ╻   \n"
GRID_COL_JOINER: str = "┃"
GRID_ROW_JOINER: str = "\n━━━╋━━━╋━━━\n"
GRID_BOTTOM: str = "\n   ╹   ╹   "

# Cell Keys
VALID_CELL_KEYS: Set[CellKey] = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
CELL_KEY_TO_CELL_MAP: Mapping[CellKey, Cell] = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
}
