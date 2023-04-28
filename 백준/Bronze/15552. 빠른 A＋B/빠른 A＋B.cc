# include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i = i + 1){
        int num1, num2;
        scanf("%d %d", &num1, &num2);
        printf("%d\n", num1 + num2);
    }
}