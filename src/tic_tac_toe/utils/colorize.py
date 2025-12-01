"""Colorize text."""

from enum import Enum, auto

from constants.constants import (
    ANSI_GREY,
    ANSI_RED,
    ANSI_GREEN,
    ANSI_CYAN,
    ANSI_YELLOW,
    ANSI_MAGENTA,
    ANSI_RESET,
)


class Color(Enum):
    """Color option enum for text colors."""

    GREY = auto()
    RED = auto()
    GREEN = auto()
    CYAN = auto()
    YELLOW = auto()
    MAGENTA = auto()


def _colorize(input_str: str, color: Color) -> str:
    """Colorize input text."""

    match color:
        case Color.GREY:
            colorized_str: str = f"{ANSI_GREY}{input_str}"
        case Color.RED:
            colorized_str = f"{ANSI_RED}{input_str}"
        case Color.GREEN:
            colorized_str = f"{ANSI_GREEN}{input_str}"
        case Color.CYAN:
            colorized_str = f"{ANSI_CYAN}{input_str}"
        case Color.YELLOW:
            colorized_str = f"{ANSI_YELLOW}{input_str}"
        case Color.MAGENTA:
            colorized_str = f"{ANSI_MAGENTA}{input_str}"
        case _:
            raise ValueError(f"Invalid color: {color!r}.")

    return f"{colorized_str}{ANSI_RESET}"


def grey(input_str: str) -> str:
    """Turn text grey."""

    return _colorize(input_str, Color.GREY)


def red(input_str: str) -> str:
    """Turn text red."""

    return _colorize(input_str, Color.RED)


def green(input_str: str) -> str:
    """Turn text green."""

    return _colorize(input_str, Color.GREEN)


def cyan(input_str: str) -> str:
    """Turn text cyan."""

    return _colorize(input_str, Color.CYAN)


def yellow(input_str: str) -> str:
    """Turn text yellow."""

    return _colorize(input_str, Color.YELLOW)


def magenta(input_str: str) -> str:
    """Turn text magenta."""

    return _colorize(input_str, Color.MAGENTA)
