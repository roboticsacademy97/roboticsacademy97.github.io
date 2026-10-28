// RA97 · ФІЗ-експрес · Arduino як вольтметр
// Плата: Arduino Uno або Nano (ATmega328P). Serial Monitor: 115200 бод.
// Надішли будь-який символ у Serial Monitor: скетч зробить серію вимірів і надрукує її як CSV.
// Міняй лише константи в блоці «Налаштування».

// ---- Налаштування ----
const long UREF_MV = 5000;   // опорна напруга АЦП, мВ: впиши виміряну мультиметром між 5V і GND
const int N = 20;            // кількість вимірів у серії
const int PAUSE_MS = 50;     // пауза між вимірами, мс
const int CHANNELS = 1;      // 1 — лише A0; 2 — A0 і A1 (поглиблений рівень: ВАХ світлодіода)
// -----------------------

int series = 0;

// Код АЦП (0–1023) у мілівольти: крок квантування = UREF_MV / 1024.
float toMillivolts(int adc) {
  return adc * (float)UREF_MV / 1024.0;
}

// Перший вимір після перемикання каналу АЦП буває неточним, тому його відкидаємо.
int readChannel(uint8_t pin) {
  analogRead(pin);
  return analogRead(pin);
}

void printReading(int adc) {
  Serial.print(',');
  Serial.print(adc);
  Serial.print(',');
  Serial.print(toMillivolts(adc), 1);
}

void setup() {
  Serial.begin(115200);
  Serial.println("# Надішли будь-який символ, щоб почати серію вимірів");
}

void loop() {
  if (Serial.available() == 0) return;
  delay(20);                                    // чекаємо, поки дійде весь рядок
  while (Serial.available() > 0) Serial.read(); // і викидаємо його

  series++;
  Serial.println(CHANNELS == 2 ? "series,n,adc0,u0_mV,adc1,u1_mV" : "series,n,adc0,u0_mV");
  for (int n = 1; n <= N; n++) {
    Serial.print(series);
    Serial.print(',');
    Serial.print(n);
    printReading(readChannel(A0));
    if (CHANNELS == 2) printReading(readChannel(A1));
    Serial.println();
    delay(PAUSE_MS);
  }
}
