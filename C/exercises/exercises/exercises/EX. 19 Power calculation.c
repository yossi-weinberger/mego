#include <stdio.h>
void main() {
    int i, num1, num2, num1_new;

    printf("Enter a number: ");
    scanf_s("%d", &num1);

    printf("Enter the second number: ");
    scanf_s("%d", &num2);
    num1_new = num1;

    for (i = 1; i < num2; i++)
        num1 *= num1_new;

    printf("%d  ", num1);

}
