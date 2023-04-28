#include <stdio.h>

int main(void)
{
    int C, N, score[1000];
    float A = 0, sum = 0;
    scanf("%d", &C);
    for (int i = 0; i < C; i++)
    {
        scanf("%d", &N);
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &score[j]);
            sum = sum + score[j];
        }
        sum = sum / N;
        for (int j = 0; j < N; j++)
        {
            if (sum < score[j])
            {
                A++;
            }
        }
        printf("%.3f%%\n", A / N * 100);
        A = 0, N = 0, sum = 0;
    }

    return 0;
}