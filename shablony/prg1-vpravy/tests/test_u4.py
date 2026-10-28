import pytest

from u4_tsykly import (
    count_char,
    countdown,
    extension,
    first_digit_index,
    is_palindrome,
    minutes_to_full,
    only_letters,
    sum_digits,
)


def test_count_char():
    assert count_char("FFLFRF", "F") == 4
    assert count_char("FFLFRF", "B") == 0
    assert count_char("", "F") == 0


@pytest.mark.parametrize(("n", "expected"), [(2026, 10), (0, 0), (7, 7), (999, 27)])
def test_sum_digits(n, expected):
    assert sum_digits(n) == expected


def test_countdown():
    assert countdown(3) == "3 2 1 старт"
    assert countdown(1) == "1 старт"
    assert countdown(0) == "старт"


@pytest.mark.parametrize(
    ("level", "rate", "expected"),
    [(90, 3, 4), (0, 10, 10), (100, 5, 0), (99, 1, 1), (0, 7, 15)],
)
def test_minutes_to_full(level, rate, expected):
    assert minutes_to_full(level, rate) == expected


@pytest.mark.parametrize(("text", "expected"), [("R2D2", 1), ("ESP32", 3), ("ровер", -1), ("", -1)])
def test_first_digit_index(text, expected):
    assert first_digit_index(text) == expected


def test_only_letters():
    assert only_letters("Робот, стоп!") == "Роботстоп"
    assert only_letters("ESP32-S3") == "ESPS"
    assert only_letters("") == ""


@pytest.mark.parametrize(
    ("name", "expected"),
    [("r220.csv", "csv"), ("zvit.final.md", "md"), ("README", ""), ("archive.tar.gz", "gz")],
)
def test_extension(name, expected):
    assert extension(name) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [("потоп", True), ("ровер", False), ("", True), ("a", True), ("Аа", False)],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected
