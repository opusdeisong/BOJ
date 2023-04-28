# include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i = i + 1){
   printf("%d\n", N - i);
     }
}