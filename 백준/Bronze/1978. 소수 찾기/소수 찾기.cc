#include <stdio.h> // Preprocessing directive

int main() {
	int T, cased = 0;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int num;
		scanf("%d", &num);
		if (num == 2) {
			cased++;
		}
		for (int j = 2; j < num; j++) {
			if (num % j == 0) {
				break;
			}
			if (j == num - 1) {
				cased++;
			}
		}
	}
	printf("%d", cased);
	
	return 0;
}