# include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i = i + 1){
        int num1, num2;
        scanf("%d %d", &num1, &num2);
        printf("Case #%d: %d + %d = %d\n",i + 1, num1, num2, num1 + num2);
    }
}