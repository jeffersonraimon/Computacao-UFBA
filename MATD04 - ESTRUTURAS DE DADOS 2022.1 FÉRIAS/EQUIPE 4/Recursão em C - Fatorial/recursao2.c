#include <stdio.h>
#include <stdlib.h>

int fat(int x);

int main(){

    int fatorial = 0;

    fatorial = fat(5);

    printf("%d", fatorial);

    return 0;

}

int fat(int x){
    int resultado = 0;

    if (x == 0 || x == 1){
        return 1;

    } else{

        resultado = x * fat(x - 1);

    } return resultado;
    
}