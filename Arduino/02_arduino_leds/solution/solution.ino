#include "funshield.h"

const long interval = 300;

const int amountOfLeds = 4;
const int leds[amountOfLeds] = {led1_pin, led2_pin, led3_pin, led4_pin};

void doPause(){
  unsigned long timeNow = millis();
  while (millis() < timeNow + interval) {}
}

void disco(int tail){
  digitalWrite(leds[tail], ON);
  doPause();
  digitalWrite(leds[tail], OFF);
}

void goUp(){
  for (int tail=2; tail>=0; tail--){
          if (tail==0) return;
          disco(tail);
    }
}

void goDown() {
  for (int tail=0; tail<4; tail++){
      disco(tail);
      if (tail==3) goUp();
  }
}

void setup() {
  // put your setup code here, to run once:
  for (int i=0; i<amountOfLeds; i++){
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], OFF);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  goDown();
}
