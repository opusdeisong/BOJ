#include "stdio.h"

int main(void){
    int num1, num2, num3, num4, num5;
    scanf("%d%d%d%d%d", &num1, &num2, &num3, &num4, &num5);
    if(num1 < 40){
        num1 = 40;
    }
    if(num2 < 40){
        num2 = 40;
    }
    if(num3 < 40){
        num3 = 40;
    }
    if(num4 < 40){
        num4 = 40;
    }
    if(num5 < 40){
        num5 = 40;
    }
    printf("%d", (num1 + num2 + num3 + num4 + num5) / 5);
}