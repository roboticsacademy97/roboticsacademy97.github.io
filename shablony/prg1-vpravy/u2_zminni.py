"""Заняття 2. Змінні й типи.

Кожна вправа — функція: заготовка `def ...:` уже написана, ти пишеш тіло і `return` відповідь.
Що таке функція докладно — у занятті 5.
Тести: uv run pytest tests/test_u2.py
"""


def mah_to_coulombs(mah):
    """Переводить заряд з мА·год у кулони (1 мА·год = 3,6 Кл).

    >>> mah_to_coulombs(1000)
    3600.0
    """
    raise NotImplementedError


def adc_to_mv(adc, uref_mv):
    """Переводить код 10-бітного АЦП (0–1023) у мілівольти: adc · uref_mv / 1024.

    >>> adc_to_mv(512, 5000)
    2500.0
    """
    raise NotImplementedError


def minutes_and_seconds(total_seconds):
    """Повертає рядок «М хв С с» для цілої кількості секунд. Секунди — завжди двома цифрами.

    Підказка: // і %.

    >>> minutes_and_seconds(125)
    '2 хв 05 с'
    """
    raise NotImplementedError


def wheel_distance_m(diameter_mm, turns):
    """Повертає відстань у метрах, яку проїде колесо діаметром diameter_mm за turns обертів.

    Довжина кола = π · d. Візьми π з модуля math: import math, math.pi.

    >>> round(wheel_distance_m(65, 10), 3)
    2.042
    """
    raise NotImplementedError


def is_even(n):
    """Повертає True, якщо ціле n парне, інакше False.

    >>> is_even(4)
    True
    """
    raise NotImplementedError


def label(code, value, unit):
    """Повертає підпис виміру f-рядком: код, двокрапка, значення з одним знаком після коми, одиниця.

    >>> label("U_R", 2.857, "В")
    'U_R: 2.9 В'
    """
    raise NotImplementedError
