#include <iostream>

using namespace std;

int main(){

    int valor_segundo = 0, horas = 0, minutos = 0, segundos = 0;

    cin >> valor_segundo;

    horas = valor_segundo / 3600;
    minutos = (valor_segundo - (horas * 3600)) / 60;
    segundos = valor_segundo % 60;

    cout << horas << "h " << minutos << "m " << segundos << "s" << endl;

    return 0;

}