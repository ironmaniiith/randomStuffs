int GREEN_BULB = 6; // '1'
int RED_BULB = 7; // '0'
int incomingByte = 0;   // for incoming serial data
// Store ascii values of 1s and 0s
int ONE = '1';
int ZERO = '0';
int GLOW_TIME = 5000; // Time for which the blub glows

void setup() {
  pinMode(GREEN_BULB, OUTPUT);
  pinMode(RED_BULB, OUTPUT);
  Serial.begin(9600);
  digitalWrite(GREEN_BULB, HIGH);
  digitalWrite(RED_BULB, HIGH);
}

void glowGreenBulb() {
  digitalWrite(GREEN_BULB, LOW);
  delay(GLOW_TIME);
  digitalWrite(GREEN_BULB, HIGH);
}

void glowRedBulb() {
  digitalWrite(RED_BULB, LOW);
  delay(GLOW_TIME);
  digitalWrite(RED_BULB, HIGH);
}

void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("data received: ");
    if (incomingByte == ONE) {
      Serial.println("one");
      glowGreenBulb();
    } else if (incomingByte == ZERO) {
      Serial.println("zero");
      glowRedBulb();
    }
  }
}
