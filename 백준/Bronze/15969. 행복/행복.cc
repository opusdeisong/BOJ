#include "stdio.h"

int main(void){
    int N, min, max, temp;
    scanf("%d", &N);
    scanf("%d", &temp);
    min = temp;
    max = temp;
    for (int i = 1; i < N; i++){
        scanf("%d", &temp);
        if (temp < min){
            min = temp;
        }
        if (temp > max){
            max = temp;
        }
    }
    printf("%d", max - min);
}