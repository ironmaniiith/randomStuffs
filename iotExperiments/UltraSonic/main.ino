/*
Userful links: https://www.youtube.com/watch?v=ZejQOX69K5M
Author: Aalekh Jain (ironmaniiith)

*/


const int trigPin = 9;
const int echoPin = 10;
long duration;
float oldDistance = 0.0;
float newDistance = 1.0;
float errorFactor = 0.05;

void setup()  
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  Serial.begin(9600);
}

void loop() // run over and over
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
   
  duration = pulseIn(echoPin, HIGH);
  newDistance = ((float)duration * 0.034)/2;
  if(abs(newDistance-oldDistance) >= errorFactor){
    oldDistance = newDistance;
    Serial.print("Distance: ");
    Serial.println(newDistance/2);
  }
  delay(100);
}
