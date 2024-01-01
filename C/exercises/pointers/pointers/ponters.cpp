#include<stdio.h> 
#define SIZE 16

void main() {

    char arr[] = "yossi weinberger";
    //int array[SIZE];
    int i = 0;

    char* ptr;
    ptr = &arr[0]; // ptr=arr;


    for (i = 0; i < SIZE; i++) {
        printf("%c  ", *ptr++);

    }

}
