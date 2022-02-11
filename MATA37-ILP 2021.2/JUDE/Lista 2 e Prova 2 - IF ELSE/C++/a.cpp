#include <iostream>

using namespace std;

int main(){


    int xe = 0, ye = 0, xd = 0, yd = 0;

    cin >> xe >> ye;
    cin >> xd >> yd;

    if (xe == xd && ye == yd){
        cout << "Soltar pacote";
    } else{
        cout << "Nao soltar pacote" << endl;
    }


    return 0;

}
