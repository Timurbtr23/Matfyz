#include "funshield.h"


struct Button {
    Button (int button_pin){
         pinMode(button_pin, INPUT);
     }
};


constexpr int leds[] { led4_pin, led3_pin, led2_pin, led1_pin };
constexpr int ledsCount = sizeof(leds) / sizeof(leds[0]);

constexpr int buttons[] = {button1_pin, button2_pin};
constexpr int buttonsCount = sizeof(buttons) / sizeof(buttons[0]);

constexpr int activationDelay = 1000;
constexpr int periodicDelay = 300; 

long unsigned mlls = 0;
int numberUser = 0;

bool previousButtonStates[2] = {true, true};
bool currentButtonState = true;

unsigned long currentTime[2] = {0, 0};
constexpr int changeNumberUser[2]  = {1, -1}; 
unsigned long timeCounter[2] ={0, 0};


void setup() {
  for (int i = 0; i < ledsCount; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], OFF);
  }
}


void number(int n, int btn){
  numberUser = (numberUser+changeNumberUser[btn]) % 16;
  button_func(numberUser);
}


void button_func(int counter)
{
  for (int led_number=0;led_number<4; ++led_number)
  {
    auto ledStat = counter & 1;
    counter >>= 1;
    digitalWrite(leds[led_number], ledStat?ON:OFF);
  }
}


void loop() {

  for (int button_num=0; button_num<2; ++button_num){ 
    
    currentButtonState = digitalRead(buttons[button_num]);
    mlls = millis();
    
    if (currentButtonState != previousButtonStates[button_num] && currentButtonState == false) { 
      timeCounter[button_num] = mlls;
      number(numberUser, button_num);
    }
    else if ((mlls-timeCounter[button_num]) >= activationDelay && currentButtonState == false && (mlls - currentTime[button_num]) >= periodicDelay)
    {
      currentTime[button_num] = mlls;
      number(numberUser, button_num);     
    }
    previousButtonStates[button_num] = currentButtonState;
  }
}
