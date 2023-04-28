# include <stdio.h>

int main(void)
{
    int max, count, numbers[9];
    for (int i = 0; i < 9; i++){
        scanf("%d", &numbers[i]);
        if (i == 0){
            max = numbers[i];
            count = 1;
        }
        else{
            if (numbers[i] > max){
                max = numbers[i];
                count = i + 1;
            }
        }
    }
    
    printf("%d\n%d", max, count);

}