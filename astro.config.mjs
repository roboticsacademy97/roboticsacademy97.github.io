// @ts-check
import { readFileSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { parse } from 'yaml';

// Курси в бічному меню беремо з тих самих даних, що й Карту.
/** @type {{ code: string, slug: string, name: string, track: string }[]} */
const courses = parse(readFileSync(new URL('./src/data/courses.yaml', import.meta.url), 'utf8'));
const TRACKS = { fundament: '00 Фундамент', zalizo: '01 Залізо', embedded: '02 Embedded', shi: '03 ШІ' };
const courseGroups = Object.entries(TRACKS).map(([track, label]) => ({
  label,
  collapsed: track !== 'fundament',
  items: courses
    .filter((c) => c.track === track)
    .map((c) => ({ label: `${c.code} · ${c.name}`, link: `/kursy/${c.slug}/` })),
}));

export default defineConfig({
  // Адреса сайту на GitHub Pages; зміниться, якщо буде підключено власний домен.
  site: 'https://roboticsacademy97.github.io',
  trailingSlash: 'always',
  integrations: [
    starlight({
      title: 'Академія робототехніки 97',
      description: 'Robotics Academy 97 · Lyceum No. 97, Dnipro — позаурочна інженерна програма: робототехніка, вбудовані системи, периферійний ШІ.',
      logo: {
        light: './src/assets/brand/ra97-lockup.svg',
        dark: './src/assets/brand/ra97-lockup-on-dark.svg',
        replacesTitle: true,
      },
      favicon: '/favicon.svg',
      locales: { root: { label: 'Українська', lang: 'uk' } },
      customCss: [
        '@fontsource/russo-one/400.css',
        '@fontsource-variable/manrope',
        '@fontsource-variable/jetbrains-mono',
        './src/styles/ra97.css',
      ],
      sidebar: [
        { label: 'Про академію', link: '/pro/' },
        { label: 'Вступ і діагностика', link: '/vstup/' },
        {
          label: 'Програма',
          items: [
            { label: 'Карта програми', link: '/programa/' },
            { label: 'Пілотний набір 2026', link: '/programa/pilot/' },
          ],
        },
        {
          // Навчальні матеріали модулів: уроки, завдання, бейджі. Порядок — як у пілотному наборі.
          label: 'Матеріали',
          items: [
            { label: 'БЕЗ · Безпека в майстерні', collapsed: true, items: [{ autogenerate: { directory: 'kursy/bez' } }] },
            { label: 'ФІЗ-експрес', collapsed: true, items: [{ autogenerate: { directory: 'kursy/fiz/ekspres' } }] },
            { label: 'ІНС-експрес', collapsed: true, items: [{ autogenerate: { directory: 'kursy/ins/ekspres' } }] },
            { label: 'ПРГ1 · Python I', collapsed: true, items: [{ autogenerate: { directory: 'kursy/prg/prg1' } }] },
          ],
        },
        { label: 'Курси', items: [{ label: 'Усі курси', link: '/kursy/' }, ...courseGroups] },
      ],
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
      lastUpdated: true,
    }),
  ],
});
