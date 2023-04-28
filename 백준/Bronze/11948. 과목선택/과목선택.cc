#include "stdio.h"

int main(void){
    int num1, num2, num3, num4, num5, num6, sum1, sum2;
    scanf("%d%d%d%d%d%d", &num1, &num2, &num3, &num4, &num5, &num6);
    if ((num1 <= num2) && (num1 <= num3) && (num1 <= num4))
        sum1 = num2 + num3 + num4;
    else if ((num2 <= num3) && (num2 <= num4))
        sum1 = num1 + num3 + num4;
    else if (num3 <= num4)
        sum1 = num1 + num2 + num4;
    else
        sum1 = num1 + num2 + num3;
    if (num5 >= num6)
        sum2 = num5;
    else
        sum2 = num6;
    printf("%d", sum1 + sum2);

}