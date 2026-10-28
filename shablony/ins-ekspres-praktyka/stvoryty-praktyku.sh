#!/usr/bin/env bash
# RA97 · ІНС-експрес · тренувальна тека для заняття 2 «Термінал і файлова система».
# Створює ~/praktyka з файлами для вправ. Запуск: bash stvoryty-praktyku.sh
set -euo pipefail

ROOT="$HOME/praktyka"
if [ -e "$ROOT" ]; then
  echo "Тека $ROOT уже є. Перейменуй її (mv ~/praktyka ~/praktyka-stara), щоб почати спочатку."
  exit 1
fi

mkdir -p "$ROOT"/laby/2026-11 "$ROOT"/laby/2026-12 "$ROOT"/roboty/rover "$ROOT"/roboty/manipuliator \
  "$ROOT"/logy "$ROOT"/chernetky
cd "$ROOT"

# Лабораторні: серії вимірів напруги у форматі скетча ФІЗ-експрес
make_series() { # файл, середній код АЦП
  {
    echo "series,n,adc0,u0_mV"
    for n in $(seq 1 20); do
      adc=$(( $2 - 3 + RANDOM % 7 ))
      echo "1,$n,$adc,$(( adc * 4860 / 1024 ))"
    done
  } > "$1"
}
make_series laby/2026-11/r220.csv 601
make_series laby/2026-11/r470.csv 611
make_series laby/2026-11/r1k.csv 620
make_series laby/2026-12/dilnyk.csv 512

# Журнали робота: INFO, WARN і ERROR упереміш
for d in 01 02 03; do
  for i in $(seq 1 30); do
    level=INFO
    if (( i % 7 == 0 )); then level=WARN; fi
    if (( i % 11 == 0 )); then level=ERROR; fi
    printf '2026-11-%s 10:%02d:00 %s rover: крок %d\n' "$d" "$i" "$level" "$i"
  done > "logy/rover-2026-11-$d.log"
done

# Кути сервоприводу з повторами — для sort і uniq
printf '%s\n' 90 45 135 90 0 180 45 90 30 150 > roboty/manipuliator/kuty.txt

# Скрипт без права на виконання — для chmod
cat > roboty/rover/start.sh <<'SCRIPT'
#!/usr/bin/env bash
echo "Ровер готовий до старту"
SCRIPT
chmod 644 roboty/rover/start.sh

printf '# Ровер\n\nЧернетка README.\n' > roboty/rover/README.md
printf 'Нотатки з першого заняття\n' > "chernetky/нотатки 1.txt"
printf 'Нотатки з другого заняття\n' > "chernetky/нотатки 2.txt"
printf 'Ти знайшов прихований файл.\n' > .sekret

echo "Готово: $ROOT"
