#include <stdio.h>

int main(void) {
  int n, i, j, star;
  scanf("%d", &n);
  i = 0;
  star = 0;
  int find =0;
  for(j =1; j <=n; j++){
    i = j;
    while(i){
      if(i % 10 == 3 || i % 10 == 6 ||i % 10 == 9 ){
        star++;
      //  printf("*");
        find = 1;
      }
      i = i/10;
      
    }
    if(!find){
   // printf("%d ", j);
      }
    else{
    //  printf(" ");
    }
    find = 0;
  }
   printf("%d", star);
  return 0;
}