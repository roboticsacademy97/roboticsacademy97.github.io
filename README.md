# Академія робототехніки 97 — сайт

Сайт RA97 (*Robotics Academy 97 · Lyceum No. 97, Dnipro*): програма академії, паспорти курсів і матеріали модулів.

Зроблено на [Astro](https://astro.build) і [Starlight](https://starlight.astro.build). Зміни потрапляють на сайт через pull request: перевірка **Check** має бути зеленою, зливає людина, а GitHub Actions за хвилину-дві публікує сайт.

Працюєте з AI-агентом (Claude, Codex)? Інструкції для нього — [AGENTS.md](AGENTS.md). Як додати чи змінити матеріал — [CONTRIBUTING.md](CONTRIBUTING.md).

## Що де лежить

```
src/data/            ← програма як дані: courses.yaml, modules.yaml, plan-a.yaml (повний шлях ролей)
src/content/docs/    ← сторінки: Про академію, Вступ, Карта, паспорти курсів, матеріали модулів
src/components/      ← таблиці модулів і шляхів, картки треків
src/pages/kursy/     ← сторінки курсів, для яких паспорт ще не написано (генеруються з даних)
src/styles/ra97.css  ← кольори й шрифти бренду RA97
src/assets/brand/    ← логотип і знак, не змінювати
scripts/check-program.mjs ← перевірка програми перед збиранням
```

## Запуск на своєму комп'ютері

Потрібен Node.js 24 або новіший.

```sh
npm install
npm run dev            # http://localhost:4321, сайт оновлюється під час редагування
npm run build          # перевірка програми + astro check + збирання в dist/
npm run check:program  # лише перевірка програми, за секунду
```

## Офлайн-копія

Під час тривоги інтернет у ліцеї вимикають. Після кожної публікації архів сайту оновлюється в релізі **offline** (вкладка Releases). Розпакуйте `ra97-site.zip` на флешку і запустіть:

```sh
python -m http.server -d ra97-site
```

Сайт відкриється на http://localhost:8000 разом із пошуком. Подвійний клік по `index.html` не підійде: пошук і посилання працюють лише через сервер.
