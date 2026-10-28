"""Рівень зі зірочкою: найкоротший шлях додому. Не обов'язково для бейджа."""

import pytest

from rover import EAST, NORTH, SOUTH, WEST, path_home, run

try:
    path_home(0, 0, NORTH)
except NotImplementedError:
    pytest.skip("path_home ще не написано — це рівень зі зірочкою", allow_module_level=True)
except Exception:  # помилку покажуть самі тести нижче
    pass

# (x, y, d, найменша можлива довжина рядка)
CASES = [
    (0, 0, NORTH, 0),
    (0, 2, SOUTH, 2),
    (0, 2, NORTH, 4),
    (3, 0, WEST, 3),
    (3, 0, EAST, 5),
    (2, 3, SOUTH, 6),
    (2, 3, WEST, 6),
    (2, 3, NORTH, 7),
    (2, 3, EAST, 7),
    (5, 1, NORTH, 8),
]


@pytest.mark.parametrize(("x", "y", "d", "shortest"), CASES)
def test_path_home(x, y, d, shortest):
    path = path_home(x, y, d)
    assert set(path) <= set("FLR"), "лише команди F, L, R"
    end_x, end_y, _ = run(path, 10, 10, x=x, y=y, d=d)
    assert (end_x, end_y) == (0, 0), f"рядок {path!r} не привіз ровер у (0, 0)"
    assert len(path) == shortest, f"рядок {path!r} довший за найкоротший ({shortest})"
