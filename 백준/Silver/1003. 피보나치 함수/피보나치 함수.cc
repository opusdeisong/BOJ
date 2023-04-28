#include "stdio.h"

void fibonacci(int num){
    int last = 0, result = 0, current = 1;
    for (int i = 0; i <= num; i++){
        last = current;
        current = result;
        result = last + current;
    }
    printf("%d %d\n", last, current);
}

int main(void){
    int T, N;
    scanf("%d", &T);
    for (int i = 0; i < T; i++){
        scanf("%d", &N);
        fibonacci(N);
    }
}