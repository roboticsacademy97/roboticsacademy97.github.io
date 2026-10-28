"""Поглиблений рівень: команди з числом повторів. Не обов'язково для бейджа."""

import pytest

from rover import EAST, NORTH, SOUTH, WEST, run_counted

try:
    run_counted("", 1, 1)
except NotImplementedError:
    pytest.skip("run_counted ще не написано — це поглиблений рівень", allow_module_level=True)
except Exception:  # помилку покажуть самі тести нижче
    pass


def test_without_numbers_same_as_run():
    assert run_counted("FFRF", 5, 5) == (1, 2, EAST), "без чисел працює як run"


def test_example():
    assert run_counted("F3R2", 5, 5) == (0, 3, SOUTH)


def test_two_digit_number():
    assert run_counted("F12", 20, 20) == (0, 12, NORTH), "F12 — дванадцять кроків, а не F1 і F2"


def test_zero_means_skip():
    assert run_counted("F0R0", 5, 5) == (0, 0, NORTH)


def test_numbers_and_border():
    assert run_counted("F9RF2", 3, 3) == (2, 2, EAST), "зайві кроки за межу пропускаються"


def test_turn_with_number():
    assert run_counted("L3", 5, 5) == (0, 0, EAST)


def test_long_route():
    assert run_counted("RF4LF4L2F2", 5, 5) == (4, 2, SOUTH)


@pytest.mark.parametrize("bad", ["3F", "F3X", "f3", "F 3"])
def test_rejects_bad_input(bad):
    with pytest.raises(ValueError):
        run_counted(bad, 5, 5)


def test_start_is_kept():
    assert run_counted("F2", 5, 5, x=1, y=1, d=WEST) == (0, 1, WEST)
