int interruptPin = 0;
void setup(){
	Serial.begin(9600);
	pinMode(interruptPin, INPUT);
	digitalWrite(interruptPin, 0);
	attachInterrupt(interruptPin, myInterrupt, RISING); //The interruptPin 0 is the pin number 2 of arduino
}

void loop(){
	// Pass
}

void myInterrupt(){
	Serial.println(1);
}