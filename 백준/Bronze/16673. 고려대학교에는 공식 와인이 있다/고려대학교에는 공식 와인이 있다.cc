#include "stdio.h"
int calc(int C, int K, int P){
    if (C == 0){
        return 0;
    }
    if(C == 1){
        return K + P;
    }
    else{
        return calc(C - 1, K, P) + C * P + C * C * K;
    }
}
int main(void){
    int C, K, P;
    scanf("%d %d %d", &C, &P, &K);
    printf("%d", calc(C, K, P));
}