#include <stdio.h> // Preprocessing directive

int main() {
	int num1, num2, num3, num4, num5, temp;
	scanf("%d %d %d %d %d", &num1, &num2, &num3, &num4, &num5);
	while ((num1 > num2) || (num2 > num3) || (num3 > num4) || (num4 > num5)) {
		if (num1 > num2) {
			temp = num1;
			num1 = num2;
			num2 = temp;
			printf("%d %d %d %d %d\n", num1, num2, num3, num4, num5);
		}
		if (num2 > num3) {
			temp = num2;
			num2 = num3;
			num3 = temp;
			printf("%d %d %d %d %d\n", num1, num2, num3, num4, num5);
		}
		if (num3 > num4) {
			temp = num3;
			num3 = num4;
			num4 = temp;
			printf("%d %d %d %d %d\n", num1, num2, num3, num4, num5);
		}
		if (num4 > num5) {
			temp = num4;
			num4 = num5;
			num5 = temp;
			printf("%d %d %d %d %d\n", num1, num2, num3, num4, num5);
		}
	}
	return 0;
}