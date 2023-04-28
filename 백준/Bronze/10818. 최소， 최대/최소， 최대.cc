# include <stdio.h>

int main(void)
{
    int num, temp, max, min;
    scanf("%d", &num);
    int numbers[num];
    for (int i = 0; i < num; i++){
        scanf("%d", &numbers[i]);
        if (i == 0){
            min = numbers[i];
            max = numbers[i];
        }
        else{
            if (numbers[i] < min){
                min = numbers[i];
            }
            if (numbers[i] > max){
                max = numbers[i];
            }
        }
    }
    
    printf("%d %d", min, max);

}