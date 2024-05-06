import pytest

from compare import *
from fibonacci import *
from palindrom import *
from square import *


def test_square():
    data = (
        (5, 2, '*', "*****\n"
                    "*****\n"
                    "** **\n"
                    "*****\n"
                    "*****"),
        (5, 1, '#', "#####\n"
                    "#   #\n"
                    "#   #\n"
                    "#   #\n"
                    "#####"),
    )

    for d in data:
        assert square(d[0], d[1], d[2]) == d[3], f"input: {d[0], d[1], d[2]}"


def test_compare():
    data = (
        ("", "", True),
        ("abc", "Abc", True),
        ("abc", "xyz", False),
        ("idę", "idą", False),
    )

    for d in data:
        assert compare(d[0], d[1]) == d[2], f"input: {d[0], d[1]}"


def test_palindrom():
    data = (
        ("abc", False),
        ("ara", True),
        ("Kobyła ma mały bok", True),
    )

    for d in data:
        assert palindrom(d[0]) == d[1], f"input: {d[0]}"


def test_fibonacci():
    data = (
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
    )

    for d in data:
        assert fib_r(d[0]) == d[1], f"input: {d[0]}"

    for d in data:
        assert fib_l(d[0]) == d[1], f"input: {d[0]}"
