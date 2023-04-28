#include <stdio.h>
#include <string.h>

int main(void)
{
    int num, count = 0, score = 0;
    char quiz[81];
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%s", quiz);
        score = 1, count = 0;
        for (int j = 0; j < strlen(quiz); j++)
        {
            if (quiz[j] == 'O')
            {
                count = score + count;
                score ++;
            }
            else
            {
                score = 1;
            }
        }
        printf("%d\n", count);
    }
    return 0;
}