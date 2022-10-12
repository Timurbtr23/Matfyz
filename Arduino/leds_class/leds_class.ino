#include <TimeLib.h>
#include "funshield.h"


struct Led {
    int pin;
    size_t turn_on_time;
    bool is_on;

    Led(int led_pin) {
        pin = led_pin;
        turn_on_time = 0;
        is_on = false;
    }

    void setup(){
        pinMode(pin, OUTPUT);
        turn_off();
    }

    void turn_on() {
        if (!is_on) {
          digitalWrite(pin, ON);
          is_on = true;
          turn_on_time = now();
        }
    }

    void turn_off() {
        if (is_on) {
          digitalWrite(pin, OFF);
          is_on = false;
        }
    }
};


struct Leds {
    Led leds[4] = {
      Led(led1_pin),
      Led(led2_pin),
      Led(led3_pin),
      Led(led4_pin)
    };

    int tail = -1;

    size_t size() {
        return sizeof(leds) / sizeof(leds[0]);
    }

    void setup(){
        for(size_t i=0; i<size(); i++) {
            leds[i].setup();
      }
    }

    void turn_on_next() {
        if (tail == -1) {
            leds[0].turn_on();
            tail == 0;  
            return;
        }
//        leds[tail % 4].turn_off();
//        leds[(tail+1) % 4].turn_on();
    }
};

Leds leds;
constexpr size_t TIMEOUT_MS = 1000;
size_t last_turn_on;

void setup() {
    leds.setup();
    last_turn_on = now();
}

void loop() {
    if (last_turn_on + TIMEOUT_MS >= now()) {
        leds.turn_on_next();
        last_turn_on = now();
    }
}
