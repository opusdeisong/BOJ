#include <stdio.h> //Preprocessing directive
int main(void) { //Function(main)
	int num1 = 1, num2 = 2;
	while (num1 != 0, num2 != 0) {
		scanf("%d %d", &num1, &num2);
		if (num1 == 0, num2 == 0)
			break;
		else
		{
			printf("%d\n", num1 + num2);
		}
	}
	return 0; //return statement
}