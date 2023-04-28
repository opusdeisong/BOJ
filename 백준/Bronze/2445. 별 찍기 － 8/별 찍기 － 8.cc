#include <stdio.h> // Preprocessing directive

int main() {
	int num;
	scanf("%d", &num);
	for (int i = 1; i < num; i++) {
		for (int j = 0; j < i ; j++) {
			printf("*");
		}
		for (int k = 0; k < num * 2 - i * 2; k++) {
			printf(" ");
		}
		for (int j = 0; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}
	for (int i = 0; i < num * 2; i++) {
		printf("*");
	}
	printf("\n");
	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num - 1 - i; j++) {
			printf("*");
		}
		for (int k = 0; k < 2 * i + 2; k++) {
			printf(" ");
		}
		for (int j = 0; j < num - 1 - i; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}