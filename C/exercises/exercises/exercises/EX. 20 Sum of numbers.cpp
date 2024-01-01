#include <stdio.h>
void main() {
    int i, num1, num2;

    for (i = 1; i < 6; i++) {
        printf("Enter a number: ");
        scanf_s("%d", &num2);
        num1 += num2;
    }


    printf("The sum is: %d  \n", num1);
    if (num1 < 0)
        printf("The sum is smaller than 0");
    else if (num1 > 0)
        printf("The sum is bigger than 0");
    else
        printf("The sum is 0");
}

