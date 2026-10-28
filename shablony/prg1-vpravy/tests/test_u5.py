import pytest

from u5_funktsii import (
    clamp,
    count_primes,
    is_prime,
    led_current_ma,
    motor_command,
    pwm_from_percent,
)


@pytest.mark.parametrize(
    ("value", "expected"),
    [(300, 255), (-5, 0), (0, 0), (255, 255), (128, 128)],
)
def test_clamp(value, expected):
    assert clamp(value, 0, 255) == expected


@pytest.mark.parametrize(
    ("percent", "expected"),
    [(0, 0), (50, 128), (100, 255), (-100, -255), (150, 255), (-150, -255), (10, 26)],
)
def test_pwm_from_percent(percent, expected):
    assert pwm_from_percent(percent) == expected


def test_led_current_ma_defaults():
    assert led_current_ma(220) == pytest.approx(13.636, abs=1e-3)
    assert led_current_ma(1000) == pytest.approx(3.0)


def test_led_current_ma_custom():
    assert led_current_ma(470, u_led=1.9) == pytest.approx(6.596, abs=1e-3)
    assert led_current_ma(100, u_led=3.0, u_supply=3.3) == pytest.approx(3.0)


@pytest.mark.parametrize(
    ("n", "expected"),
    [(2, True), (3, True), (4, False), (97, True), (1, False), (0, False), (91, False)],
)
def test_is_prime(n, expected):
    assert is_prime(n) is expected, f"n = {n}"


@pytest.mark.parametrize(("limit", "expected"), [(10, 4), (2, 1), (1, 0), (100, 25)])
def test_count_primes(limit, expected):
    assert count_primes(limit) == expected


def test_motor_command():
    assert motor_command(50, -100) == "L128 R-255"
    assert motor_command(0, 0) == "L0 R0"
    assert motor_command(200, 10) == "L255 R26"
