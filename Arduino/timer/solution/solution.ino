#include "funshield.h"
#include <math.h>

constexpr int buttons[] = { button1_pin, button2_pin, button3_pin };
constexpr int count_of_buttons = sizeof(buttons) / sizeof(buttons[0]);
constexpr int point = 0b01111111;


enum LedState {PRESSED, RELEASED};

class Pressed {
  public:
    Pressed(int pin) { pin1 = pin; }
    
    bool pressedOnce(bool ifPressed) {
      if (ifPressed == false)
      {
        PreviousState = RELEASED;
        return false;
      }
      
      if (PreviousState == PRESSED && ifPressed)
        return false;
        
      PreviousState = PRESSED;
      return true;
    }
    
  private:
    LedState PreviousState = RELEASED;
    int pin1;
};

Pressed pressed[]
{
  Pressed(button1_pin),
  Pressed(button2_pin),
  Pressed(button3_pin)
};
//////////////////////////////////////////////////////////////////

struct Display {
    void write_glyph(int glyph, int position) {
      digitalWrite(latch_pin, LOW);
      shiftOut(data_pin, clock_pin, MSBFIRST, glyph);
      shiftOut(data_pin, clock_pin, MSBFIRST, position);
      digitalWrite(latch_pin, HIGH);
    }
    void showTime(int thousands, int hundreds, int sec, int ms){
        write_glyph( ms, digit_muxpos[3] );
        write_glyph( sec & point, digit_muxpos[2] );
        
        if ((hundreds  != digits[0]) || (thousands != digits[0]))  write_glyph( hundreds, digit_muxpos[1] );
        if (thousands != digits[0])                                                write_glyph( thousands, digit_muxpos[0] );
    }
};

Display display;
/////////////////////////////////////////////////////////////////

struct Timer {
  int count = 0;
  int ms = digits[0];
  int s    = digits[0];
  int hs = 0xFF;
  int ts  = 0xFF;
  
    void update_info(){
        ms = digits[count % 10];
        s    = digits[count / 10];

        if (count >= 100) {
          s  = digits[count / 10 % 10];
          hs = digits[count / 100];
        }

        if (count >= 1000) {
          s  = digits[count / 10 % 100 % 10];
          hs = digits[count / 100 % 10];
           ts = digits[count / 1000];
        }
     }

    void go() {
        count+=1;
        update_info();
    }

    void reset(){
        count = 0;
        ms = digits[0];
        s    = digits[0];
        hs = 0xFF;
        ts  = 0xFF;
    }
};

Timer timer;
/////////////////////////////////////////////////////////////////

int status = -1;


void setup() {
    for (int i = 0; i < count_of_buttons; ++i)
    {
      pinMode(buttons[i], INPUT);
    }
    pinMode(latch_pin, OUTPUT);
    pinMode(clock_pin, OUTPUT);
    pinMode(data_pin, OUTPUT);
}

unsigned long currTime;
unsigned long previousMillis = 0; 

int count_for_status = 0;

void loop() {
  currTime = millis();

    if ( pressed[0].pressedOnce(!digitalRead(buttons[0])) || (pressed[1].pressedOnce(!digitalRead(buttons[1]))) ){
        count_for_status += 1;
        status = count_for_status % 2;
    }

    if (pressed[2].pressedOnce(!digitalRead(buttons[2])) && (status == 0))
        status = -1;


    if (status == 1){
      if (currTime - previousMillis >= 100) {
            previousMillis = currTime;
            timer.go();
        }
    }
    else if (status == 0) {
    }
    else {
        timer.reset();
        count_for_status = 0;
    }
    display.showTime(timer.ts, timer.hs, timer.s, timer.ms);
}
