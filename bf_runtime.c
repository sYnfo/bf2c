#include <stdio.h>

#define INCD() ++data;
#define DECD() --data;
#define INC() ++*data;
#define DEC() --*data;
#define PRINT() putchar(*data);
#define IN() *data = getchar();
#define JUMPF() while (*data) {
#define JUMPB() };

char memory[30000];
char* data = memory;

int main() {
    #include "bf.c"
    return 0;}
