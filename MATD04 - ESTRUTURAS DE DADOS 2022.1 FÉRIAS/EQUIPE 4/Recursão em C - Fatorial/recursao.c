#include <stdio.h>
#include "fatorialRecursivo.h"

/*

FATORIAL

5! = 5 * 4 * 3 * 2 * 1 = 120
.
.
0! = 1! = 1

*/

int factRecursivo(int x);

int main(void) {

    int fatorial = 0;

    fatorial = factRecursivo(5);
	
	printf("%d\n", fatorial);
    printf("\n");

	return 0;
}

