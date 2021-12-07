#include <iostream>

using namespace std;

int main(){

    int N, C, D, U, modC, modD, modU;

    cin >> N;

    U = N / 1;
    modU = U % 10;

    D = N / 10;
    modD = D % 10;

    C = N / 100;
    modC = C % 10;
    cout << modU << " " << modD << " " << modC;

}

