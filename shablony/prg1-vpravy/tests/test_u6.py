import pytest

from u6_nalahodzhennia import average_speed, need_charge, percent


def test_average_speed():
    assert average_speed("10 20 30", 6) == pytest.approx(10.0)
    assert average_speed("50", 5) == pytest.approx(10.0)


@pytest.mark.parametrize(
    ("voltage", "minutes", "expected"),
    [(3.4, 30, True), (3.8, 5, True), (3.8, 30, False), (3.4, 5, True)],
)
def test_need_charge(voltage, minutes, expected):
    assert need_charge(voltage, minutes) is expected


@pytest.mark.parametrize(("part", "whole", "expected"), [(1, 3, 33.3), (1, 2, 50.0), (3, 3, 100.0)])
def test_percent(part, whole, expected):
    assert percent(part, whole) == pytest.approx(expected)
