int pin = 8;
int count=0;

void setup() {
	pinMode(pin, INPUT);
	Serial.begin(9600);
}

void loop() {
	int a = digitalRead(pin);
	if(a==1){
		if(count>=5){
			count=0;
			Serial.println(1);
		}
		else{
			count++;
		}
	}
}