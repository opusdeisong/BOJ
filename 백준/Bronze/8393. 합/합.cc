# include <stdio.h>

int main(void)
{
    int N, sum = 0;
    scanf("%d", &N);
    for (int i = 1; i < N + 1;i = i + 1){
        sum = sum + i;
    }
    printf("%d", sum);
}