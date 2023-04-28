# include <stdio.h>

int main(void)
{
    int N, X, num1;
    scanf("%d %d", &N, &X);
    for (int i = 1; i <= N; i = i + 1){
        scanf("%d ", &num1);
        if (num1 < X)
            printf("%d ", num1);    
    }
}