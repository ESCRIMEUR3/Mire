int mods_actifs[4] = {};

void setup() {
  // put your setup code here, to run once:
  pinMode(22, INPUT);
  pinMode(23, INPUT);
  pinMode(24, INPUT);

  pinMode(25, INPUT);
  pinMode(26, INPUT);
  pinMode(27, INPUT);

  pinMode(28, INPUT);
  pinMode(29, INPUT);
  pinMode(30, INPUT);

  pinMode(31, INPUT);
  pinMode(32, INPUT);
  pinMode(33, INPUT);

  for (int i=0; i<10; i += 3) {
    if (digitalRead(22+i) == LOW && digitalRead(23+i) == LOW && digitalRead(24+i) == LOW){
      mods_actifs[i/3] = 1;
    }
    if (digitalRead(22+i) == LOW && digitalRead(23+i) == LOW && digitalRead(24+i) == HIGH){
      mods_actifs[i/3] = 2;
    }
    if (digitalRead(22+i) == LOW && digitalRead(23+i) == HIGH && digitalRead(24+i) == LOW){
      mods_actifs[i/3] = 3;
    }
    if (digitalRead(22+i) == LOW && digitalRead(23+i) == HIGH && digitalRead(24+i) == HIGH){
      mods_actifs[i/3] = 4;
    }
    if (digitalRead(22+i) == HIGH && digitalRead(23+i) == LOW && digitalRead(24+i) == LOW){
      mods_actifs[i/3] = 5;
    }
    if (digitalRead(22+i) == HIGH && digitalRead(23+i) == LOW && digitalRead(24+i) == HIGH){
      mods_actifs[i/3] = 6;
    }
    if (digitalRead(22+i) == HIGH && digitalRead(23+i) == HIGH && digitalRead(24+i) == LOW){
      mods_actifs[i/3] = 7;
    }
    if (digitalRead(22+i) == HIGH && digitalRead(23+i) == HIGH && digitalRead(24+i) == HIGH){
      mods_actifs[i/3] = 8;
    }
  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(mods_actifs[0]);
  Serial.println(mods_actifs[1]);
  Serial.println(mods_actifs[2]);
  Serial.println(mods_actifs[3]);
}
