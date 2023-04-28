#include <stdio.h> //Preprocessing directive
int main(void) { //Function(main)
	int N, NN = 0, i = 1;
	scanf("%d", &N);
	if (N % 10 >= N / 10) {
		NN = N / 10 + (N % 10 - N / 10) * 10;
	}
	else{
		NN = N / 10 + (N % 10 - N / 10 + 10) * 10;

	}
		while (N != NN) {
		N = (N / 10 + N % 10) % 10 + (N % 10) * 10;
		i = i + 1;
	}
	printf("%d", i);
	return 0; //return statement
}