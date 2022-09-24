#include <stdio.h>

void print_stars(int n, int all) {

  int space = (all - n) / 2;
  for (size_t i = 0; i < space; i++) {
    printf(" ");
  }

  for (int i = 0; i <= n; i++) {
    printf("*");
  }
}


void print_trepezoid(int k, int all){
  for (size_t i = 0; i < all; i+=2) {
    if (k > 0) {
      k -= 1;
    }
    else {
      print_stars(i, all);  printf("\n");
    }
  }
}


int main(){
  
  int k = 20;
  int all = 69;

  print_trepezoid(k, all);

  return 0;
}
