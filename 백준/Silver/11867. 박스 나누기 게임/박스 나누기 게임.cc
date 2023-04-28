#include <stdio.h> // Preprocessing directive

int main() {
	int A, B;
	scanf("%d %d", &A, &B);
	if ((A % 2 == 0) || (B % 2 == 0)) {
		printf("A");
	}
	else {
		printf("B");
	}
	return 0;
}