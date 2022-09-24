#include <funshield.h>

int ledState = OFF;  

unsigned long previousMillis = 0;
const long interval = 100;

const int leds[4] = {led1_pin, led2_pin, led3_pin, led4_pin};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(leds[0], OUTPUT); 
  pinMode(leds[1], OUTPUT);
  pinMode(leds[2], OUTPUT);
  pinMode(leds[3], OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
   unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    // if the LED is off turn it on and vice-versa:
    if (ledState == OFF) {
      ledState = ON;
    } else {
      ledState = OFF;
    }
  
  digitalWrite(led1_pin, ledState); // sets the digital pin 13 on
  digitalWrite(led2_pin, ledState);
  digitalWrite(led3_pin, ledState);
  digitalWrite(led4_pin, ledState);
  }
}
