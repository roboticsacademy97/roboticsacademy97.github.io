import { defineCollection } from 'astro:content';
import { file } from 'astro/loaders';
import { z } from 'astro/zod';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Програма академії як дані (id запису = slug): з цих файлів збираються Карта, таблиці курсів і сторінки модулів.
// Перехресні перевірки (пререквізити, цикли, порядок у шляху) — у scripts/check-program.mjs.

const tracks = ['fundament', 'zalizo', 'embedded', 'shi'] as const;

const courses = defineCollection({
  loader: file('src/data/courses.yaml'),
  schema: z.object({
    code: z.string(),            // ПРГ — як у тексті
    slug: z.string(),            // prg — як в адресі
    name: z.string(),
    track: z.enum(tracks),
    modules: z.array(z.string()).nonempty(),
    passport: z.string().optional(), // версія паспорта, якщо він уже на сайті
  }),
});

const modules = defineCollection({
  loader: file('src/data/modules.yaml'),
  schema: z.object({
    code: z.string(),            // ПРГ1, МАТ1.2, ROS.1
    slug: z.string(),            // prg1, mat1-2, ros1
    course: z.string(),          // slug курсу
    name: z.string(),
    topics: z.string().optional(),
    year: z.string(),            // рік у повній траєкторії: '0', '1', '2–3'
    when: z.string().optional(), // уточнення: «кінець»
    prereqs: z.array(z.string()),
    hours: z.number().int().positive().optional(),
    who: z.string(),             // ядро · шлях: … · вступ: … · за вибором
    outcomes: z.string().optional(),
    badge: z.string().optional(),
    extern: z.boolean().optional(),
  }),
});

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema() }),
  courses,
  modules,
};
