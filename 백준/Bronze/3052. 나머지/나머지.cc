# include <stdio.h>

int main(void)
{
    int temp[10], num[42], count;
    count = 0;
    for (int j = 0; j < 42; j ++){
        num[j] = 0;
        }
        
    for (int i = 0; i < 10; i ++){
        scanf("%d", &temp[i]);
        num[temp[i] % 42] ++;
        }
    
    for (int j = 0; j < 42; j ++){
        if (num[j] != 0){
            count ++;
            }
         }
    printf("%d", count);
    return 0;
}