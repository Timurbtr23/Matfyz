#include <stdio.h>


int main(){

  int window = 3;
  int data[] = {3,4,4,5,6,8,11,11,10,5,2,0};
  int lenTeps = sizeof(data) / sizeof(data[0]);
  int avg = 0;

  for (size_t k = 0; k < lenTeps-2; k++) {
    for (int i = 0; i < window; i++) {
      avg += data[k+i];
    }
    avg /= window;
    printf("%d\n", avg);
    avg = 0;
  }

  return 0;
}
