#include <funshield.h>

int ledState = OFF;  

unsigned long previousMillis = 0;
const long interval = 1000;

const int leds[4] = {led1_pin, led2_pin, led3_pin, led4_pin};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(leds[0], OUTPUT); 
  pinMode(leds[1], OUTPUT);
  pinMode(leds[2], OUTPUT);
  pinMode(leds[3], OUTPUT);

  digitalWrite(leds[0], OFF);
  digitalWrite(leds[1], OFF);
  digitalWrite(leds[2], OFF);
  digitalWrite(leds[3], OFF);
}

void loop() {
  // put your main code here, to run repeatedly:
   unsigned long currentMillis = millis();

   for (int tail=0; tail<4; tail++){
      digitalWrite(leds[tail], ON);
      if (tail==3) {digitalWrite(leds[0], ON);}
      else {digitalWrite(leds[tail+1], ON);}
      
      delay(400);
      
      digitalWrite(leds[tail], OFF);
      if (tail==3) {digitalWrite(leds[0], OFF);}
      else {digitalWrite(leds[tail+1], OFF);}
   }
}
