#include "stdio.h"
int main(void){
    int num, temp, a = 0, b = 0, c = 0, d = 0, len = 0;
    scanf("%d", &num);
    while (num != 0){
        temp = num % 10;
        if (temp == 0){
            a++;
        }
        if (temp == 1){
            b++;
        }
        if (temp == 2){
            c++;
        }
        if (temp == 8){
            d++;
        }
        num = num / 10;
        len ++;
    }
    if ((a + b + c + d) == len){
        if ((a > 0) && (b > 0) && (c > 0) && (d > 0)){
            if ((a == b) && (b == c) && (c == d)){
                printf("8");
            }
            else{
                printf("2");
            }
        }
        else{
            printf("1");
        }
    }
    else{
        printf("0");
    }
}