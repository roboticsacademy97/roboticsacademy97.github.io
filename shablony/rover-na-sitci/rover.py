"""Ровер на сітці — бейдж ПРГ1 і завдання діагностики.

Поле має width клітинок у ширину і height у висоту.
Клітинка (0, 0) — лівий нижній кут, x росте праворуч, y — угору.
Напрям ровера — ціле число 0–3: північ, схід, південь, захід.

Заміни кожне `raise NotImplementedError` своїм кодом.
Обов'язковий рівень — шість функцій угорі файлу. Решта — для тих, хто хоче більше.
Повна умова: https://roboticsacademy97.github.io/kursy/prg/rover-na-sitci/
"""

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


# ---------- Обов'язковий рівень ----------


def turn_left(d):
    """Повертає новий напрям після повороту ліворуч на 90°.

    >>> turn_left(NORTH) == WEST
    True
    """
    raise NotImplementedError


def turn_right(d):
    """Повертає новий напрям після повороту праворуч на 90°.

    >>> turn_right(WEST) == NORTH
    True
    """
    raise NotImplementedError


def step(x, y, d):
    """Повертає координати (x, y) клітинки на один крок попереду.

    Межі поля тут не перевіряються.

    >>> step(2, 2, EAST)
    (3, 2)
    """
    raise NotImplementedError


def inside(x, y, width, height):
    """Повертає True, якщо клітинка (x, y) лежить на полі width × height.

    >>> inside(0, 0, 3, 2)
    True
    >>> inside(3, 0, 3, 2)
    False
    """
    raise NotImplementedError


def run(commands, width, height, x=0, y=0, d=NORTH):
    """Виконує рядок команд і повертає кінцевий стан (x, y, d).

    F — крок уперед, L — поворот ліворуч, R — поворот праворуч.
    Крок за межу поля ровер пропускає: лишається на місці й виконує наступну команду.
    Будь-який інший символ, навіть пробіл чи мала літера, — помилка ValueError.

    >>> run("FFRF", 5, 5)
    (1, 2, 1)
    """
    raise NotImplementedError


def report(x, y, d):
    """Повертає стан ровера рядком «x y напрям», напрям — літерою N, E, S або W.

    >>> report(1, 2, EAST)
    '1 2 E'
    """
    raise NotImplementedError


# ---------- Поглиблений рівень ----------


def run_counted(commands, width, height, x=0, y=0, d=NORTH):
    """Як run, але після команди може стояти число повторів: «F3R2» = «FFFRR».

    Число може мати кілька цифр («F12»); 0 означає «не виконувати».
    Цифра на початку рядка або невідома літера — ValueError.

    >>> run_counted("F3R2", 5, 5)
    (0, 3, 2)
    """
    raise NotImplementedError


def run_on_map(commands, grid, x=0, y=0, d=NORTH):
    """Виконує команди F/L/R на карті з перешкодами.

    grid — список рядків однакової довжини: '.' — вільно, '#' — перешкода.
    grid[0] — верхній ряд поля, тобто клітинка (x, y) — це grid[len(grid) - 1 - y][x].
    У перешкоду, як і за межу поля, ровер не їде.

    >>> run_on_map("FF", ["..", "#.", ".."])
    (0, 0, 0)
    """
    raise NotImplementedError


# ---------- Зі зірочкою ----------


def path_home(x, y, d):
    """Повертає найкоротший рядок команд F/L/R, що веде ровер зі стану (x, y, d) у (0, 0).

    Поле без перешкод, кінцевий напрям — будь-який.

    >>> path_home(0, 2, SOUTH)
    'FF'
    """
    raise NotImplementedError


# ---------- Запуск вручну: uv run rover.py ----------


def main():
    width, height = input("Розмір поля (ширина висота): ").split()
    commands = input("Команди: ")
    x, y, d = run(commands, int(width), int(height))
    print(report(x, y, d))


if __name__ == "__main__":
    main()
