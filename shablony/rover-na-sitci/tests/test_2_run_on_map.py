"""Поглиблений рівень: карта з перешкодами. Не обов'язково для бейджа."""

import pytest

from rover import EAST, NORTH, SOUTH, run_on_map

try:
    run_on_map("", ["."])
except NotImplementedError:
    pytest.skip("run_on_map ще не написано — це поглиблений рівень", allow_module_level=True)
except Exception:  # помилку покажуть самі тести нижче
    pass

# Поле 4 × 3. Верхній рядок списку — це y = 2, нижній — y = 0.
MAP = [
    "..#.",
    ".#..",
    "....",
]


def test_free_way():
    assert run_on_map("RFFF", MAP) == (3, 0, EAST)


def test_obstacle_stops_step():
    assert run_on_map("RFLF", MAP) == (1, 0, NORTH), "клітинка (1, 1) зайнята"


def test_obstacle_then_continue():
    assert run_on_map("FFRFF", MAP) == (1, 2, EAST), "(2, 2) зайнята, другий крок пропущено"


def test_border_on_map():
    assert run_on_map("FFFF", MAP) == (0, 2, NORTH), "межа поля діє і на карті"


def test_rows_are_counted_from_top():
    grid = ["#...", "....", "...."]
    assert run_on_map("FF", grid) == (0, 1, NORTH), "grid[0] — верхній ряд, тож зайнята (0, 2)"


def test_from_given_start():
    assert run_on_map("FF", MAP, x=3, y=2, d=SOUTH) == (3, 0, SOUTH)
