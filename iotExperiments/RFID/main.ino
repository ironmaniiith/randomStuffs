#include <SoftwareSerial.h>

SoftwareSerial RFID(10, 11); // RX, TX

void setup()  
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
  // set the data rate for the SoftwareSerial port
  RFID.begin(9600);
}

void loop() // run over and over
{
  if(RFID.available()){
    while (RFID.available()){
      Serial.write(RFID.read());
    }
    Serial.println();
  }  
}
