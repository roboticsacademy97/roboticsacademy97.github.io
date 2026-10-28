"""Заняття 4. Цикли і рядки.

Методи рядків на кшталт .count(), .find() чи .replace() у цих вправах не використовуй:
мета — написати цикл самому. Індекси, зрізи, len() і in — можна.
Тести: uv run pytest tests/test_u4.py
"""


def count_char(text, char):
    """Повертає, скільки разів символ char трапляється в text.

    >>> count_char("FFLFRF", "F")
    4
    """
    raise NotImplementedError


def sum_digits(n):
    """Повертає суму цифр невід'ємного цілого n. Без str(): лише //, % і while.

    >>> sum_digits(2026)
    10
    """
    raise NotImplementedError


def countdown(n):
    """Повертає рядок зворотного відліку від n до 1 через пробіл і слово «старт».

    >>> countdown(3)
    '3 2 1 старт'
    """
    raise NotImplementedError


def minutes_to_full(level, rate):
    """Скільки хвилин заряджати акумулятор від level відсотків, якщо щохвилини додається rate.

    Зарядка триває, поки рівень менший за 100. level від 0 до 100, rate > 0.

    >>> minutes_to_full(90, 3)
    4
    """
    raise NotImplementedError


def first_digit_index(text):
    """Повертає індекс першої цифри в text або -1, якщо цифр немає. Цикл зупини break.

    >>> first_digit_index("R2D2")
    1
    """
    raise NotImplementedError


def only_letters(text):
    """Повертає text без пробілів і розділових знаків — лише літери. Перевірка: символ.isalpha().

    >>> only_letters("Робот, стоп!")
    'Роботстоп'
    """
    raise NotImplementedError


def extension(filename):
    """Повертає розширення файла — частину після останньої крапки — або "", якщо крапки немає.

    >>> extension("r220.csv")
    'csv'
    """
    raise NotImplementedError


def is_palindrome(text):
    """Повертає True, якщо text однаково читається в обидва боки (з урахуванням регістру).

    >>> is_palindrome("потоп")
    True
    """
    raise NotImplementedError
