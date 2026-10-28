"""Заняття 6. Налагодження: у кожній функції є одна помилка.

Тести вже показують, що щось не так: uv run pytest tests/test_u6.py
Знайди помилку налагоджувачем VS Code: точка зупинки (клік ліворуч від номера рядка),
Run → Start Debugging (F5) або кнопка налагодження тесту, далі крок за кроком (F10, F11)
і стеж за значеннями змінних. Виправ лише помилку — решту коду не переписуй.
"""


def average_speed(distances_cm, seconds):
    """Середня швидкість у см/с: сума всіх відстаней, поділена на загальний час.

    distances_cm — рядок чисел через пробіл, наприклад "10 20 30".

    >>> average_speed("10 20 30", 6)
    10.0
    """
    total = 0
    parts = distances_cm.split()
    for i in range(1, len(parts)):
        total = total + int(parts[i])
    return total / seconds


def need_charge(cell_voltage, minutes_left):
    """Чи треба ставити акумулятор на зарядку.

    Так, якщо напруга банки нижча за 3,5 В або роботі лишилося працювати менше 10 хв.

    >>> need_charge(3.4, 30)
    True
    """
    return cell_voltage < 3.5 and minutes_left < 10


def percent(part, whole):
    """Яку частку у відсотках part становить від whole, з точністю до десятих.

    >>> percent(1, 3)
    33.3
    """
    return round(part // whole * 100, 1)
