# include <stdio.h>

int main(void)
{
    int A, B, C, D, num[10], temp;
    scanf("%d\n%d\n%d", &A, &B, &C);
    D = A * B * C;
    if (D / 1000000000 == 0){
        num[0] = -1;}
    if (D / 100000000 == 0){
        num[0] = -2;}
    if (D / 10000000 == 0){
        num[0] = -3;}
    for (int i = 1; i < 10; i ++){
        num[i] = 0;
    }
    for (int i = 1000000000; i > 0; i = i / 10){
        temp = D / i;
        num[temp] = num[temp] + 1;
        D = D % i;
    }
    for (int i = 0; i < 10; i++){
        printf("%d\n", num[i]);
    }

}