#include "stdio.h"
#include "math.h"

int main(void){
    int D, H, W;
    double DD;
    scanf("%d %d %d", &D, &H, &W);
    DD = sqrt((H * H) + (W * W));
    printf("%d %d", int(D * H / DD), int(D * W / DD));
}