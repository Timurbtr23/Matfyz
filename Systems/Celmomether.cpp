#include <stdio.h>
#include "temps.h"

void print_stars(int val, int min_val) {

  int space = min_val * -1;

  if (val <= 0) {
    space += val;

    for (int i = 0; i < space; i++) {
      printf(" ");
    }

    val *= -1;
    for (int i = 0; i < val; i++) {
      printf("*");
    }

    printf("|");
  }

  else {
    for (int i = 0; i < space; i++) {
      printf(" ");
    }

    printf("|");

    for (int i = 0; i < val; i++) {
      printf("*");
    }
  }
}


void print_values(int len, int min_val){
  int last_temp = 0;

  for (int i = 0; i < len; i++) {
    if (temperatures[i] == no_value) {
        print_stars(last_temp, min_val);
    }
    else {
        print_stars(temperatures[i], min_val);
    }

    printf("\n");
    if (temperatures[i] != no_value) last_temp = temperatures[i];
  }
}


int min_temperature(int len){
  int min_value = 999;

  for (int i = 0; i < len; i++) {
    if ((temperatures[i] < min_value) & (temperatures[i] != no_value))
        min_value = temperatures[i];
  }

  return min_value;
}


int main(){

  int lenTemperaturs = sizeof(temperatures) / sizeof(temperatures[0]);
  int min_temp = min_temperature(lenTemperaturs);

  print_values(lenTemperaturs, min_temp);

  return 0;
}
