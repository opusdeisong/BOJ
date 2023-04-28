#include <stdio.h> // Preprocessing directive

int main() {
	int T;
	int arr[20000] = { 0,1 };
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int num;
		scanf("%d", &num);
		for (int j = 2; j <= num; j++) {
			for (int k = 2; j * k <= num; k++) {
				arr[j * k] = 1;
			}
		}
		for (int m = num / 2; m > 0; m--) {
			if (arr[m] != 1 && arr[num - m] != 1) {
				printf("%d %d\n", m, num - m);
				break;
			}
		}
	}
	return 0;
}