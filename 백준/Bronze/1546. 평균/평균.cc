#include <stdio.h>

int main(void) {
    int num;
    float sum = 0, score[1000], max = 0;
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        scanf("%f", &score[i]);
        if (max < score[i]) {
            max = score[i];
        }
    }
    for (int j = 0; j < num; j++) {
        score[j] = (float)score[j] / max * 100;
    }
    for (int k = 0; k < num; k++) {
        sum = sum + score[k];
    }
    printf("%f", (float)sum / num);
    return 0;
}