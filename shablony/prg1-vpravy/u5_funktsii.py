"""Заняття 5. Функції і декомпозиція.

Тут уже є готові функції, які можна викликати з інших: так ділять задачу на частини.
Тести: uv run pytest tests/test_u5.py
"""


def clamp(value, low, high):
    """Обмежує value межами [low, high]: менше low — low, більше high — high, інакше value.

    >>> clamp(300, 0, 255)
    255
    """
    raise NotImplementedError


def pwm_from_percent(percent):
    """Переводить швидкість мотора у відсотках (-100…100) у ШІМ-значення (-255…255).

    Результат — ціле, округлене функцією round().
    Відсотки поза -100…100 спершу обмеж функцією clamp.

    >>> pwm_from_percent(50)
    128
    """
    raise NotImplementedError


def led_current_ma(r_ohm, u_led=2.0, u_supply=5.0):
    """Повертає струм через світлодіод у міліамперах: (u_supply - u_led) / r_ohm · 1000.

    Параметри u_led і u_supply мають значення за замовчуванням.

    >>> round(led_current_ma(220), 1)
    13.6
    """
    raise NotImplementedError


def is_prime(n):
    """Повертає True, якщо ціле n — просте число (ділиться лише на 1 і на себе, n ≥ 2).

    >>> is_prime(97)
    True
    """
    raise NotImplementedError


def count_primes(limit):
    """Повертає, скільки простих чисел від 2 до limit включно. Використай is_prime.

    >>> count_primes(10)
    4
    """
    raise NotImplementedError


def motor_command(left_percent, right_percent):
    """Будує команду для двох моторів: «L<шім> R<шім>», де шім — з pwm_from_percent.

    >>> motor_command(50, -100)
    'L128 R-255'
    """
    raise NotImplementedError
