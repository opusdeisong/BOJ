#include "stdio.h"

int find_thedate(int num){
    if (num == 1)
        return 0;
    else if (num == 3)
        return find_thedate(num - 1) + 28;
    else if ((num == 5) || (num == 7) || (num == 10) || (num == 12))
        return find_thedate(num - 1) + 30;
    else
        return find_thedate(num - 1) + 31;
}
int main(void){
    int month, date;
    scanf("%d %d", &month, &date);
    date = find_thedate(month) + date;
    if (date % 7 == 1)
        printf("MON");
    else if (date % 7 == 2)
        printf("TUE");
    else if (date % 7 == 3)
        printf("WED");
    else if (date % 7 == 4)
        printf("THU");
    else if (date % 7 == 5)
        printf("FRI");
    else if (date % 7 == 6)
        printf("SAT");
    else if (date % 7 == 0)
        printf("SUN");

}