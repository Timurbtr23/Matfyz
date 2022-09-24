#include "funshield.h"

int leds[4] = {led1_pin, led2_pin, led3_pin, led4_pin};

unsigned long time;
unsigned int pause = 300;
unsigned int cycle = 1800;

void setup() {
  for (int i = 0; i < 4; ++i){
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
    
    time = millis();
    
    if (time  == 0) digitalWrite(leds[0], ON);

    for (int i = 1; i < 4; ++i){
      if (time % cycle == i*pause )
      {
        digitalWrite(leds[i-1], OFF);
        digitalWrite(leds[i], ON);
      }
    }

    for(int i = 3; i > 1; --i){
      if (time % cycle == (7 -i)*pause)
      {
        digitalWrite(leds[i], OFF);
        digitalWrite(leds[i-1], ON);
      }
    }

    if (time % cycle == 0 )
    {
      digitalWrite(leds[1], OFF);
      digitalWrite(leds[0], ON);
    }
}
