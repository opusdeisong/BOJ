#include <stdio.h>

int main(void){
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++){
        int num;
        scanf("%d", &num);
        printf("%d\n", num * 23);
    }
    return 0;
}