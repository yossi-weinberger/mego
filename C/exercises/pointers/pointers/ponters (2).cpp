#include<stdio.h> 
#define SIZE 16
#include<time.h>

void main() {

    srand(time(NULL));
    int randNumber;

    char arr[] = "yossi weinberger";
    //int array[SIZE];
    int i = 0;

    char* ptr;
    ptr = &arr[0]; // ptr=arr;


    for (i = 0; i < SIZE; i++) {
        printf("%c  ", *ptr++);

    }

}
