#include "stdio.h"

int Rev(int num){
    int new_num = 0;
    while(num != 0){
        new_num = new_num * 10 + num % 10;
        num = num / 10;
    }
    return new_num;
}

int main(void){
    int num1, num2, ans;
    scanf("%d %d", &num1, &num2);
    ans = Rev(Rev(num1) + Rev(num2));
    printf("%d", ans);
}