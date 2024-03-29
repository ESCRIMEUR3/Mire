#include <Arduino.h>

int ID_board = 145;
char tab[3][10]; // Déclaration d'un tableau 2D pour stocker les chaînes de caractères

void setup() {
  Serial.begin(9600);
  pinMode(A1, INPUT);
  snprintf(tab[0], 10, "%d", ID_board); // Conversion de ID_board en chaîne de caractères et stockage dans tab[0]
}

int Analyse() {
  int mods_actifs = 0; // Déclaration et initialisation du tableau pour stocker les codes d'état

  if (digitalRead(22) == LOW && digitalRead(23) == LOW && digitalRead(24) == LOW) {
    mods_actifs = 0;
  } else if (digitalRead(22) == LOW && digitalRead(23) == LOW && digitalRead(24) == HIGH) {
      mods_actifs = 1;
  } else if (digitalRead(22) == LOW && digitalRead(23) == HIGH && digitalRead(24) == LOW) {
      mods_actifs = 2;
  } else if (digitalRead(22) == LOW && digitalRead(23) == HIGH && digitalRead(24) == HIGH) {
      mods_actifs = 3;
  } else if (digitalRead(22) == HIGH && digitalRead(23) == LOW && digitalRead(24) == LOW) {
      mods_actifs = 4;
  } else if (digitalRead(22) == HIGH && digitalRead(23) == LOW && digitalRead(24) == HIGH) {
      mods_actifs = 5;
  } else if (digitalRead(22) == HIGH && digitalRead(23) == HIGH && digitalRead(24) == LOW) {
      mods_actifs = 6;
  } else if (digitalRead(22) == HIGH && digitalRead(23) == HIGH && digitalRead(24) == HIGH) {
      mods_actifs = 7;
  }
  return mods_actifs;
}

void loop() {
  int mods = Analyse(); // Récupération des codes d'état
  float sensorVal = analogRead(A1);
  float valfinal = 0; // Initialisation de la variable valfinal à l'extérieur de la condition

  if (mods == 4) { // Utiliser '==' pour la comparaison, pas '='
    float voltage = (sensorVal / 1024.0) * 5.0;
    valfinal = (voltage - 0.5) * 100; // Stocker la valeur dans la variable valfinal
  } else if (mods == 2) { // Utiliser '==' pour la comparaison, pas '='
    valfinal = (sensorVal / 1023.0) * 100; // Utiliser 1023.0 pour assurer une division flottante
  }

  snprintf(tab[1], 10, "%d", mods); // Stockage des codes d'état dans tab[1]
  snprintf(tab[2], 10, "%d", (int)round(valfinal)); // Conversion de la température en chaîne de caractères et stockage dans tab[2]
  Serial.println(String(tab[0]) + ":" + String(tab[1]) + "=" + String(tab[2])); // Envoi des données via la communication série
  delay(100);
}
