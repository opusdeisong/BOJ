#include <stdio.h>

int main(void)
{
    int one, two, three;
    scanf("%d %d %d", &one, &two, &three);
    if (one == two and one == three)
        printf("%d", 10000 + 1000 * one);
    else
        if (one == two or one == three)
            printf("%d", 1000 + 100 * one);
        else
            if (two == three)
                printf("%d", 1000 + 100 * two);
            else
                if (one > two and one > three)
                    printf("%d", one * 100);
                else
                    if(two > three)
                        printf("%d", two * 100);
                    else
                        printf("%d", three * 100);
}