#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        if (i != 0)
            printf("\n");
        for (int j = 0; j < i; j ++){
            printf(" ");
        }
        for (int k = 2 * n; k > 2 * i + 1; k--) {
            printf("*");
        }
    }
}