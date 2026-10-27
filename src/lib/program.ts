import { getCollection, type CollectionEntry } from 'astro:content';
import { parse } from 'yaml';
import coursesYaml from '../data/courses.yaml?raw';

export type Module = CollectionEntry<'modules'>['data'];
export type Course = CollectionEntry<'courses'>['data'];

export const TRACKS = {
  fundament: { number: '00', name: 'Фундамент' },
  zalizo: { number: '01', name: 'Залізо' },
  embedded: { number: '02', name: 'Embedded' },
  shi: { number: '03', name: 'ШІ' },
} as const;

// getCollection не зберігає порядок записів у файлі, а курси мають іти так, як їх записано.
const COURSE_ORDER: string[] = (parse(coursesYaml) as { slug: string }[]).map((c) => c.slug);

/** Уся програма: курси в порядку src/data/courses.yaml. */
export async function getProgram() {
  const courses = (await getCollection('courses'))
    .map((e) => e.data)
    .sort((a, b) => COURSE_ORDER.indexOf(a.slug) - COURSE_ORDER.indexOf(b.slug));
  const modules = (await getCollection('modules')).map((e) => e.data);
  const byCode = new Map(modules.map((m) => [m.code, m]));
  const courseOf = (m: Module) => courses.find((c) => c.slug === m.course)!;
  const modulesOf = (c: Course) => c.modules.map((code) => byCode.get(code)!);
  /** Модулі, для яких цей модуль є пререквізитом. */
  const opens = (m: Module) => modules.filter((x) => x.prereqs.includes(m.code));
  return { courses, modules, byCode, courseOf, modulesOf, opens };
}

/** Адреса модуля: розділ на сторінці його курсу. */
export const moduleHref = (m: Module) => `/kursy/${m.course}/#${m.slug}`;
