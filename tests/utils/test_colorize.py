"""Test suite for text colorization utilities."""

import unittest

from constants.constants import (
    ANSI_GREY,
    ANSI_RED,
    ANSI_GREEN,
    ANSI_CYAN,
    ANSI_YELLOW,
    ANSI_MAGENTA,
    ANSI_RESET,
)

from tic_tac_toe.utils.colorize import grey, red, green, cyan, yellow, magenta


class TestColorize(unittest.TestCase):

    def setUp(self) -> None:
        self.test_string: str = "Hello, World!"

    def test_grey_makes_grey_text(self) -> None:
        self.assertEqual(
            grey(self.test_string), f"{ANSI_GREY}{self.test_string}{ANSI_RESET}"
        )

    def test_red_makes_red_text(self) -> None:
        self.assertEqual(
            red(self.test_string), f"{ANSI_RED}{self.test_string}{ANSI_RESET}"
        )

    def test_green_makes_green_text(self) -> None:
        self.assertEqual(
            green(self.test_string), f"{ANSI_GREEN}{self.test_string}{ANSI_RESET}"
        )

    def test_cyan_makes_cyan_text(self) -> None:
        self.assertEqual(
            cyan(self.test_string), f"{ANSI_CYAN}{self.test_string}{ANSI_RESET}"
        )

    def test_yellow_makes_yellow_text(self) -> None:
        self.assertEqual(
            yellow(self.test_string), f"{ANSI_YELLOW}{self.test_string}{ANSI_RESET}"
        )

    def test_magenta_makes_magenta_text(self) -> None:
        self.assertEqual(
            magenta(self.test_string), f"{ANSI_MAGENTA}{self.test_string}{ANSI_RESET}"
        )
