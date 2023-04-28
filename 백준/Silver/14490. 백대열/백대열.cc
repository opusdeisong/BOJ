#include <stdio.h> // Preprocessing directive

int main() {
	int num1, num2, temp, num;
	scanf("%d:%d", &num1, &num2);
	if (num1 <= num2) {
		temp = num1;
	}
	else
		temp = num2;
	for (int i = 1; i <= temp; i++) {
		if ((num1 % i == 0) && (num2 % i == 0))
			num = i;
	}
	printf("%d:%d", num1 / num, num2 / num);
	return 0;
}