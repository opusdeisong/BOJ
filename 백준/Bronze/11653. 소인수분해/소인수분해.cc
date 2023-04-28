#include <stdio.h> // Preprocessing directive

int main() {
	int num;
	scanf("%d", &num);
	while (num > 1) {
		for (int i = 2; i <= num;) {
			if (num % i == 0) {
				printf("%d\n", i);
				num = num / i;
				continue;
			}
			else {
				i++;
			}
		}
	}
	return 0;
}