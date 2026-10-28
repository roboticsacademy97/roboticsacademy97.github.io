import pytest

from u2_zminni import (
    adc_to_mv,
    is_even,
    label,
    mah_to_coulombs,
    minutes_and_seconds,
    wheel_distance_m,
)


def test_mah_to_coulombs():
    assert mah_to_coulombs(1000) == pytest.approx(3600)
    assert mah_to_coulombs(1) == pytest.approx(3.6)
    assert mah_to_coulombs(0) == 0


@pytest.mark.parametrize(
    ("adc", "uref", "expected"),
    [(0, 5000, 0.0), (512, 5000, 2500.0), (1023, 5000, 4995.1171875), (512, 4860, 2430.0)],
)
def test_adc_to_mv(adc, uref, expected):
    assert adc_to_mv(adc, uref) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [
        (125, "2 хв 05 с"),
        (60, "1 хв 00 с"),
        (59, "0 хв 59 с"),
        (0, "0 хв 00 с"),
        (3600, "60 хв 00 с"),
    ],
)
def test_minutes_and_seconds(seconds, expected):
    assert minutes_and_seconds(seconds) == expected


def test_wheel_distance_m():
    assert wheel_distance_m(65, 10) == pytest.approx(2.042, abs=1e-3)
    assert wheel_distance_m(100, 1) == pytest.approx(0.3142, abs=1e-4)
    assert wheel_distance_m(65, 0) == 0


@pytest.mark.parametrize(("n", "expected"), [(4, True), (7, False), (0, True), (-3, False)])
def test_is_even(n, expected):
    assert is_even(n) is expected


def test_label():
    assert label("U_R", 2.857, "В") == "U_R: 2.9 В"
    assert label("I", 6, "мА") == "I: 6.0 мА"
