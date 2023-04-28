#include <stdio.h> // Preprocessing directive

int main() {
	int num;
	scanf("%d", &num);
	for (int i = 0; i < num ; i++) {
		for (int j = 0; j < num - 1 - i; j++) {
			printf(" ");
		}
		for (int k = 0; k < 2 * i + 1; k++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}