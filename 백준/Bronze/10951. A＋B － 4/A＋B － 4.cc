#include <stdio.h> //Preprocessing directive
int main(void) { //Function(main)
	int num1 = 1, num2 = 2;
	while (scanf("%d %d", &num1, &num2) != -1) {
		printf("%d\n", num1 + num2);
		
	}
	return 0; //return statement
}