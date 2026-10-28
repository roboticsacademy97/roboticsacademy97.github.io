import pytest

from u3_umovy import avoid_obstacle, battery_status, close_enough, in_range, leap_year, sign


@pytest.mark.parametrize(("x", "expected"), [(3, 1), (-2.5, -1), (0, 0), (0.001, 1)])
def test_sign(x, expected):
    assert sign(x) == expected


@pytest.mark.parametrize(
    ("voltage", "expected"),
    [
        (4.2, "повний"),
        (4.0, "повний"),
        (3.99, "нормальний"),
        (3.7, "нормальний"),
        (3.69, "низький"),
        (3.3, "низький"),
        (3.29, "критичний"),
        (2.5, "критичний"),
    ],
)
def test_battery_status(voltage, expected):
    assert battery_status(voltage) == expected, f"для {voltage} В"


@pytest.mark.parametrize(
    ("value", "expected"),
    [(5, True), (0, True), (10, True), (-1, False), (10.5, False)],
)
def test_in_range(value, expected):
    assert in_range(value, 0, 10) is expected


@pytest.mark.parametrize(
    ("year", "expected"),
    [(2028, True), (2026, False), (1900, False), (2000, True), (2100, False)],
)
def test_leap_year(year, expected):
    assert leap_year(year) is expected, f"рік {year}"


def test_close_enough():
    assert close_enough(0.1 + 0.2, 0.3, 1e-9) is True
    assert close_enough(2.5, 2.6, 0.05) is False
    assert close_enough(2.5, 2.6, 0.2) is True
    assert close_enough(-1.0, 1.0, 1.5) is False


@pytest.mark.parametrize(
    ("distance", "left", "right", "expected"),
    [
        (50, False, False, "вперед"),
        (21, False, False, "вперед"),
        (20, True, True, "ліворуч"),
        (15, False, True, "праворуч"),
        (5, False, False, "назад"),
    ],
)
def test_avoid_obstacle(distance, left, right, expected):
    assert avoid_obstacle(distance, left, right) == expected
