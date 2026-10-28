"""Заняття 3. Умови.

Тести: uv run pytest tests/test_u3.py
"""


def sign(x):
    """Повертає 1 для додатного x, -1 для від'ємного і 0 для нуля.

    >>> sign(-2.5)
    -1
    """
    raise NotImplementedError


def battery_status(cell_voltage):
    """Повертає стан банки LiPo за її напругою у вольтах.

    4,0 В і більше — "повний"; від 3,7 В — "нормальний"; від 3,3 В — "низький";
    нижче 3,3 В — "критичний". Межа належить вищому стану: рівно 3,7 В — "нормальний".

    >>> battery_status(3.85)
    'нормальний'
    """
    raise NotImplementedError


def in_range(value, low, high):
    """Повертає True, якщо low ≤ value ≤ high. Спробуй записати одним порівнянням.

    >>> in_range(5, 0, 10)
    True
    """
    raise NotImplementedError


def leap_year(year):
    """Повертає True для високосного року.

    Рік високосний, якщо ділиться на 4, але не на 100, — або якщо ділиться на 400.

    >>> leap_year(2028)
    True
    """
    raise NotImplementedError


def close_enough(a, b, tolerance):
    """Повертає True, якщо a і b відрізняються не більше ніж на tolerance.

    Числа з комою (float) не порівнюють через ==: 0.1 + 0.2 == 0.3 дає False.

    >>> close_enough(0.1 + 0.2, 0.3, 1e-9)
    True
    """
    raise NotImplementedError


def avoid_obstacle(distance_cm, left_free, right_free):
    """Вирішує, куди їхати роботу перед перешкодою.

    Якщо попереду вільно (distance_cm більше за 20) — "вперед".
    Інакше: вільно ліворуч — "ліворуч"; інакше вільно праворуч — "праворуч"; інакше — "назад".

    >>> avoid_obstacle(15, False, True)
    'праворуч'
    """
    raise NotImplementedError
