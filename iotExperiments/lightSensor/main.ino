int pin = 8;
int count=0;
void setup() {
	Serial.begin(9600);
	pinMode(pin, INPUT);
}

void loop() {
	int a = digitalRead(8);
	if(a == 1){
		if(count >= 5){
			Serial.println(a);
			count=0;
		}
		else{
			count++;
		}
	}

}