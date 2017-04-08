#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);

int pin = 8;
int count=0;
String msg = "Hello World!";
int counter = 0;
void setup() {
	Serial.begin(9600);
	pinMode(pin, INPUT);
	lcd.begin(16,2);
	lcd.clear();
}

void loop() {
	int a = digitalRead(8);
	if(a == 1){
		if(count >= 5){
			Serial.println(a);
			printLCD(counter);
			count=0;
                        counter+=1;
		}
		else{
			count++;
		}
	}

}

void printLCD (int c) {
        String msg = String(c, 10);
	lcd.clear();
        lcd.print("Counter: ");
        lcd.print(msg);
	delay(1000);
}