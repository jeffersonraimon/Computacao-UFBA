#include <iostream>

using namespace std;

int main(){

    int a = 0, b = 0, c = 0, qtd = 0;

    cin >> a >> b >> c;

    qtd = a * b;

    if (qtd > c) {
        cout << "S" << endl;
    } else {
        cout << "N" << endl;
    }


    return 0;

}