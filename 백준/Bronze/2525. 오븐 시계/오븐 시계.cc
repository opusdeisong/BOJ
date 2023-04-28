#include <stdio.h>

int main(void)
{
    int hour, minute, time;
    scanf("%d %d", &hour, &minute);
    scanf("%d", &time);
    minute = minute + time;
    if (minute > 60);
        hour = hour + minute / 60;
        minute = minute % 60;
        if (hour > 23);
            hour = hour % 24;
    printf("%d %d", hour, minute);
}