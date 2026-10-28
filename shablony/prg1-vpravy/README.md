# ПРГ1 · вправи

Вправи модуля ПРГ1 (Python I) Академії робототехніки 97 з готовими тестами.
Пояснення до кожного заняття: <https://roboticsacademy97.github.io/kursy/prg/prg1/>

## Що в теці

| Файл | Заняття |
| --- | --- |
| `u1_pryvit.py`, `u1_traceback.py` | 1. Середовище і traceback |
| `u2_zminni.py`, `u2_kalkuliator.py` | 2. Змінні й типи |
| `u3_umovy.py` | 3. Умови |
| `u4_tsykly.py` | 4. Цикли і рядки |
| `u5_funktsii.py` | 5. Функції |
| `u6_nalahodzhennia.py` | 6. Тести і налагодження |
| `tests/` | готові тести до кожного заняття — не змінюй їх |

## Як запустити

Відкрий цю теку у VS Code (File → Open Folder) і в терміналі виконай:

```sh
uv run pytest tests/test_u2.py   # тести одного заняття
uv run pytest                    # усі тести
uv run ruff check .              # перевірка стилю
uv run u2_kalkuliator.py         # запустити програму
```

Тест червоний — читай повідомлення: там написано, що функція повернула і що мала повернути.
Поки функцію не написано, її тести падають з `NotImplementedError` — це нормально.
