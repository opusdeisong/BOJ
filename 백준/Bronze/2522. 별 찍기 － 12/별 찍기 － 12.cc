#include "stdio.h"

int main(void){
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i ++){
        for (int j = 0; j < N - 1 - i; j ++){
            printf(" ");
        }
        for (int k = 0; k < 1 + i; k++){
            printf("*");
        }
        printf("\n");
    }
    for (int i = 1; i < N; i ++){
        for (int j = 0; j < i; j++){
            printf(" ");
        }
        for (int k = 0; k < N - i; k++){
            printf("*");
        }
        printf("\n");
    }
}