#include <stdio.h>

int main() {

    int a[1001] = { 0, };
    int num, sum = 0, max = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &num);
        sum += num;
        a[num / 10]++;
    }
    sum = sum / 10;
    for (int i = 0; i < 100; i++) {
        if (a[i] > max)
            max = i;
    }
    printf("%d %d", sum, max * 10);


}
