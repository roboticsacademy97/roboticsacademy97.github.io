// Перевірка програми перед збиранням: пререквізити існують, циклів немає,
// у повному шляху (варіант А) жоден модуль не стоїть раніше за свій пререквізит,
// і в кожному блоці не більше двох активних модулів (слоти Ф і Т).
// Запуск: node scripts/check-program.mjs (входить у npm run build).
import { readFileSync } from 'node:fs';
import { parse } from 'yaml';

const load = (name) => parse(readFileSync(new URL(`../src/data/${name}`, import.meta.url), 'utf8'));
const modules = load('modules.yaml');
const courses = load('courses.yaml');
const plan = load('plan-a.yaml');

const errors = [];
const byCode = new Map(modules.map((m) => [m.code, m]));
const STUDIO = 'СТУДІЯ';

// 1. Кожен пререквізит і кожен модуль курсу існують, кожен модуль належить своєму курсу.
for (const m of modules) {
  for (const p of m.prereqs) if (!byCode.has(p)) errors.push(`${m.code}: невідомий пререквізит ${p}`);
  const course = courses.find((c) => c.slug === m.course);
  if (!course) errors.push(`${m.code}: невідомий курс ${m.course}`);
  else if (!course.modules.includes(m.code)) errors.push(`${m.code}: немає у списку модулів курсу ${course.code}`);
}
for (const c of courses) for (const code of c.modules) if (!byCode.has(code)) errors.push(`${c.code}: невідомий модуль ${code}`);

// 2. Циклів немає.
const state = new Map();
const visit = (code, path) => {
  if (state.get(code) === 'done') return;
  if (state.get(code) === 'open') return errors.push(`цикл пререквізитів: ${[...path, code].join(' → ')}`);
  state.set(code, 'open');
  for (const p of byCode.get(code)?.prereqs ?? []) visit(p, [...path, code]);
  state.set(code, 'done');
};
for (const m of modules) visit(m.code, []);

// 3. Повний шлях кожної ролі: порядок і ліміт.
for (const role of Object.values(plan.roles)) {
  const blocks = [];
  for (let i = 0; i < 6; i++) blocks.push([plan.year0.first[i], plan.year0.second[i]]);
  for (const y of [1, 2, 3]) for (let i = 0; i < 6; i++) blocks.push([plan.fundament[y][i], role.years[y][i]]);
  const when = new Map();
  blocks.forEach((pair, t) => {
    const active = pair.filter(Boolean);
    if (active.length > 2) errors.push(`${role.name}: у блоці ${t + 1} більше двох модулів`);
    for (const code of active) {
      if (code === STUDIO) continue;
      if (!byCode.has(code)) errors.push(`${role.name}: невідомий модуль ${code} у шляху`);
      if (when.has(code)) errors.push(`${role.name}: ${code} стоїть у шляху двічі`);
      when.set(code, t);
    }
  });
  for (const [code, t] of when) {
    for (const p of byCode.get(code)?.prereqs ?? []) {
      if (!when.has(p)) errors.push(`${role.name}: ${code} потребує ${p}, якого немає в шляху`);
      else if (when.get(p) >= t) errors.push(`${role.name}: ${code} стоїть раніше за свій пререквізит ${p} або в тому ж блоці`);
    }
  }
  if (!errors.length) console.log(`✓ ${role.name}: повний шлях — ${when.size} модулів`);
}

if (errors.length) {
  console.error(`Програма містить помилки (${errors.length}):\n- ${errors.join('\n- ')}`);
  process.exit(1);
}
console.log(`✓ Програма: модулів — ${modules.length}, курсів — ${courses.length}; пререквізити й шляхи узгоджені`);
