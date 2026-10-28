"""Обов'язковий рівень: ці тести мають пройти всі, щоб бейдж (і екстерн) зарахували."""

import pytest

from rover import EAST, NORTH, SOUTH, WEST, inside, report, run, step, turn_left, turn_right


@pytest.mark.parametrize(
    ("d", "expected"),
    [(NORTH, WEST), (WEST, SOUTH), (SOUTH, EAST), (EAST, NORTH)],
)
def test_turn_left(d, expected):
    assert turn_left(d) == expected, f"ліворуч від {d} має бути {expected}"


@pytest.mark.parametrize(
    ("d", "expected"),
    [(NORTH, EAST), (EAST, SOUTH), (SOUTH, WEST), (WEST, NORTH)],
)
def test_turn_right(d, expected):
    assert turn_right(d) == expected, f"праворуч від {d} має бути {expected}"


def test_four_turns_come_back():
    d = NORTH
    for _ in range(4):
        d = turn_left(d)
    assert d == NORTH, "чотири повороти ліворуч мають повернути на північ"


@pytest.mark.parametrize(
    ("d", "expected"),
    [(NORTH, (2, 3)), (EAST, (3, 2)), (SOUTH, (2, 1)), (WEST, (1, 2))],
)
def test_step(d, expected):
    assert step(2, 2, d) == expected, f"крок із (2, 2) у напрямку {d}"


def test_step_ignores_borders():
    assert step(0, 0, WEST) == (-1, 0), "step не перевіряє межі — це робота inside"


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        (0, 0, True),
        (2, 1, True),
        (3, 0, False),
        (0, 2, False),
        (-1, 0, False),
        (0, -1, False),
    ],
)
def test_inside(x, y, expected):
    assert inside(x, y, 3, 2) == expected, f"клітинка ({x}, {y}) на полі 3 × 2"


def test_run_empty():
    assert run("", 5, 5) == (0, 0, NORTH), "порожній рядок — ровер стоїть на старті"


def test_run_forward():
    assert run("FFF", 5, 5) == (0, 3, NORTH)


def test_run_turns_only():
    assert run("RRR", 5, 5) == (0, 0, WEST), "три повороти праворуч = один ліворуч"


def test_run_example():
    assert run("FFRF", 5, 5) == (1, 2, EAST)


def test_run_square():
    assert run("FRFRFRFR", 5, 5) == (0, 0, NORTH), "квадрат 1 × 1 повертає на старт"


def test_run_skips_step_over_border():
    assert run("FFFFFF", 5, 3) == (0, 2, NORTH), "за верхню межу поля 5 × 3 не виїжджаємо"


def test_run_continues_after_border():
    assert run("LFFRF", 4, 4) == (0, 1, NORTH), "після пропущених кроків команди виконуються далі"


def test_run_from_given_start():
    assert run("FLF", 5, 5, x=2, y=2, d=EAST) == (3, 3, NORTH)


def test_run_one_cell_field():
    assert run("FRFRF", 1, 1) == (0, 0, SOUTH), "на полі 1 × 1 жоден крок неможливий"


@pytest.mark.parametrize("bad", ["X", "f", "F F", "F1"])
def test_run_rejects_unknown_command(bad):
    with pytest.raises(ValueError):
        run(bad, 5, 5)


@pytest.mark.parametrize(
    ("x", "y", "d", "expected"),
    [(0, 0, NORTH, "0 0 N"), (1, 2, EAST, "1 2 E"), (4, 0, SOUTH, "4 0 S"), (3, 3, WEST, "3 3 W")],
)
def test_report(x, y, d, expected):
    assert report(x, y, d) == expected
