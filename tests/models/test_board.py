"""Test suite for Board."""

import unittest

from copy import deepcopy
from typing import List

from constants.constants import CellValue, BOARD_SIZE

from tic_tac_toe.models.board import Board, InvalidCellError, InvalidMoveError

from tic_tac_toe.utils.colorize import grey, red, green

TEST_BOARD_STATE: List[List[CellValue]] = [
    ["X", "O", None],
    ["O", None, "X"],
    [None, "X", "O"],
]  # NB: Do not change! Test cases depend on this.


class TestBoardGetBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_get_board_returns_correctly_sized_board(self) -> None:
        board: List[List[CellValue]] = self.board.get_board()

        self.assertEqual(len(board), BOARD_SIZE)
        for row in board:
            self.assertEqual(len(row), BOARD_SIZE)


class TestBoardGetCell(unittest.TestCase):

    def setUp(self) -> None:
        test_board_state: List[List[CellValue]] = deepcopy(TEST_BOARD_STATE)
        self.board = Board(starting_state=test_board_state)

    def test_get_cell_raises_invalid_cell_error_if_invalid_cell_provided(
        self,
    ) -> None:
        with self.assertRaises(InvalidCellError):
            self.board.get_cell((-1, 0))  # type: ignore[arg-type]

        with self.assertRaises(InvalidCellError):
            self.board.get_cell((0, -1))  # type: ignore[arg-type]

        with self.assertRaises(InvalidCellError):
            self.board.get_cell((BOARD_SIZE + 1, 0))  # type: ignore[arg-type]

        with self.assertRaises(InvalidCellError):
            self.board.get_cell((0, BOARD_SIZE + 1))  # type: ignore[arg-type]

    def test_get_cell_returns_correct_value_if_valid_cell_provided(
        self,
    ) -> None:
        self.assertEqual(self.board.get_cell((0, 0)), "X")
        self.assertEqual(self.board.get_cell((1, 1)), None)
        self.assertEqual(self.board.get_cell((2, 2)), "O")


class TestBoardMakeMove(unittest.TestCase):

    def setUp(self) -> None:
        test_board_state: List[List[CellValue]] = deepcopy(TEST_BOARD_STATE)
        self.board = Board(starting_state=test_board_state)

    def test_make_move_raises_invalid_cell_error_if_invalid_cell_attempted(
        self,
    ) -> None:
        with self.assertRaises(InvalidCellError):
            self.board.make_move((-1, 0), "X")  # type: ignore[arg-type]

        with self.assertRaises(InvalidCellError):
            self.board.make_move((0, BOARD_SIZE + 1), "O")  # type: ignore[arg-type]

    def test_make_move_raises_invalid_move_error_if_nonblank_cell_attempted(
        self,
    ) -> None:
        with self.assertRaises(InvalidMoveError):
            self.board.make_move((0, 0), "O")

        with self.assertRaises(InvalidMoveError):
            self.board.make_move((2, 2), "X")

    def test_make_move_raises_invalid_move_error_if_invalid_move_attempted(
        self,
    ) -> None:
        with self.assertRaises(InvalidMoveError):
            self.board.make_move((0, 2), "Y")  # type: ignore[arg-type]

    def test_make_move_correctly_changes_board_state(self) -> None:
        self.board.make_move((0, 2), "X")
        self.assertEqual(self.board.get_cell((0, 2)), "X")

        self.board.make_move((1, 1), "O")
        self.assertEqual(self.board.get_cell((1, 1)), "O")


class TestBoardStringifyBoard(unittest.TestCase):

    def setUp(self) -> None:
        test_board_state: List[List[CellValue]] = deepcopy(TEST_BOARD_STATE)
        self.board = Board(starting_state=test_board_state)

    def test_stringify_board_returns_proper_board_string(self) -> None:
        actual_board_string = self.board.stringify_board()

        top: str = "   ╻   ╻   "
        row1: str = f"{red(' X ')}┃{green(' O ')}┃{grey(' 9 ')}"
        joiner: str = "━━━╋━━━╋━━━"
        row2: str = f"{green(' O ')}┃{grey(' 5 ')}┃{red(' X ')}"
        row3: str = f"{grey(' 1 ')}┃{red(' X ')}┃{green(' O ')}"
        bottom: str = "   ╹   ╹   "

        correct_board_string: str = (
            f"{top}\n{row1}\n{joiner}\n{row2}\n{joiner}\n{row3}\n{bottom}"
        )

        self.assertEqual(actual_board_string, correct_board_string)


class TestBoardCheckWin(unittest.TestCase):

    def test_check_win_detects_horizontal_win(self) -> None:
        horizontal_win_state_1: List[List[CellValue]] = [
            ["X", "X", "X"],
            ["O", None, "O"],
            [None, None, "O"],
        ]

        horizontal_win_state_1_board: Board = Board(
            starting_state=horizontal_win_state_1
        )
        self.assertEqual(horizontal_win_state_1_board.check_win(), (True, "X"))

        horizontal_win_state_2: List[List[CellValue]] = [
            [None, "X", "X"],
            ["X", None, None],
            ["O", "O", "O"],
        ]

        horizontal_win_state_2_board: Board = Board(
            starting_state=horizontal_win_state_2
        )
        self.assertEqual(horizontal_win_state_2_board.check_win(), (True, "O"))

    def test_check_win_detects_vertical_win(self) -> None:
        vertical_win_state_1: List[List[CellValue]] = [
            ["O", "X", None],
            ["O", "X", "X"],
            ["O", "O", None],
        ]

        vertical_win_state_1_board: Board = Board(starting_state=vertical_win_state_1)
        self.assertEqual(vertical_win_state_1_board.check_win(), (True, "O"))

        vertical_win_state_2: List[List[CellValue]] = [
            ["O", None, "X"],
            [None, "O", "X"],
            ["O", None, "X"],
        ]

        vertical_win_state_2_board: Board = Board(starting_state=vertical_win_state_2)
        self.assertEqual(vertical_win_state_2_board.check_win(), (True, "X"))

    def test_check_win_detects_diagonal_wins(self) -> None:
        diagonal_win_state_1: List[List[CellValue]] = [
            ["O", "X", None],
            ["X", "O", "X"],
            [None, None, "O"],
        ]

        diagonal_win_state_1_board: Board = Board(starting_state=diagonal_win_state_1)
        self.assertEqual(diagonal_win_state_1_board.check_win(), (True, "O"))

        diagonal_win_state_2: List[List[CellValue]] = [
            [None, "O", "X"],
            ["O", "X", "O"],
            ["X", None, None],
        ]

        diagonal_win_state_2_board: Board = Board(starting_state=diagonal_win_state_2)
        self.assertEqual(diagonal_win_state_2_board.check_win(), (True, "X"))

    def test_check_win_detects_non_win(self) -> None:
        non_win_state: List[List[CellValue]] = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"],
        ]

        non_win_state_board: Board = Board(starting_state=non_win_state)
        self.assertEqual(non_win_state_board.check_win(), (False, None))
