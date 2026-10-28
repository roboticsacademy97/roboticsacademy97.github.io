import { readdirSync, readFileSync } from 'node:fs';
import { join, relative } from 'node:path';
import type { APIRoute, GetStaticPaths } from 'astro';
import { zipSync, type Zippable } from 'fflate';

// Шаблони завдань лежать текою в shablony/<name>/, а учні отримують їх архівом /shablony/<name>.zip.
// Архів збирається під час build, тож офлайн-копія сайту містить і шаблони.

const ROOT = join(process.cwd(), 'shablony');
const SKIP = new Set(['.venv', '__pycache__', '.pytest_cache', '.ruff_cache', '.DS_Store']);
// Фіксована дата у файлах архіву: однаковий вміст — однаковий zip.
const MTIME = new Date('2026-01-01T00:00:00Z');

function files(dir: string): string[] {
  return readdirSync(dir, { withFileTypes: true })
    .filter((e) => !SKIP.has(e.name))
    .flatMap((e) => (e.isDirectory() ? files(join(dir, e.name)) : [join(dir, e.name)]))
    .sort();
}

export const getStaticPaths = (() =>
  readdirSync(ROOT, { withFileTypes: true })
    .filter((e) => e.isDirectory())
    .map((e) => ({ params: { name: e.name } }))) satisfies GetStaticPaths;

export const GET: APIRoute = ({ params }) => {
  const name = params.name!;
  const dir = join(ROOT, name);
  const tree: Zippable = {};
  for (const path of files(dir)) {
    tree[`${name}/${relative(dir, path).split('\\').join('/')}`] = [readFileSync(path), { mtime: MTIME }];
  }
  return new Response(zipSync(tree, { level: 9 }), {
    headers: { 'Content-Type': 'application/zip' },
  });
};
