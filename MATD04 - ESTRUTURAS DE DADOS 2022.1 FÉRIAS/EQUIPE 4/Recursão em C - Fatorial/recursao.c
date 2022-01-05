#include <stdio.h>
#include "fatorialRecursivo.h"
//include "fatorialLoop.h"

//int factloop(int x);

int factRecursivo(int x);

int main(void) {

    int fatorial = 0;

    fatorial = factRecursivo(5);
	
	printf("%d\n", fatorial);
    printf("\n");

	return 0;
}

