#include "funshield.h"
#include <math.h>

constexpr int count_of_pos = 4;
constexpr int buttons[] = { button1_pin, button2_pin, button3_pin };
constexpr int count_of_buttons = sizeof(buttons) / sizeof(buttons[0]);

enum LedState {PRESSED, RELEASED};

int counter   = 0;
int position1 = 0;
int number    = 0;

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


void Write (byte glyph, byte pos_bitmask) {
  digitalWrite( latch_pin, LOW);
  shiftOut( data_pin, clock_pin, MSBFIRST, glyph);
  shiftOut( data_pin, clock_pin, MSBFIRST, pos_bitmask);
  digitalWrite( latch_pin, HIGH);
}


void WriteDigits (int number, int pos) {
  Write(digits[number], digit_muxpos[count_of_pos - pos - 1]);
}


int Digit (int number, int position) {
    if ( ((int)log10(number) < position) || (position < 0))
        return 0;
    else
        return (number % (int)(pow(10, position + 1))) / (int)( pow(10, position));
}


Pressed pressed[]
{
  Pressed(button1_pin),
  Pressed(button2_pin),
  Pressed(button3_pin)
};


void setup() {
  for (int i = 0; i < count_of_buttons; ++i)
  {
    pinMode(buttons[i], INPUT);
  }
  pinMode(latch_pin, OUTPUT);
  pinMode(data_pin, OUTPUT);
  pinMode(clock_pin, OUTPUT);
}


void loop() {
    
  if (pressed[0].pressedOnce(!digitalRead(buttons[0])))
  {
        counter += pow (10, position1);
        if (counter >= 10000) 
          counter %= 10000;
  }
    
  if ((pressed[1].pressedOnce(!digitalRead(buttons[1]))))
  {
      counter -= pow (10, position1);
      if (counter < 0) 
        counter = 10000 + (counter % 10000);
  }
  
  if (pressed[2].pressedOnce(!digitalRead(buttons[2])))
    position1 += 1;
  
  position1 %= 4;
  number = Digit(counter, position1);
  WriteDigits(number, position1);
}
