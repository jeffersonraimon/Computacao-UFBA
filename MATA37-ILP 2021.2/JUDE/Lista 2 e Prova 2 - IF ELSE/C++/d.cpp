#include <iostream>

using namespace std;

int main(){

    char zagueiro, goleiro, direcao, chute;

    cin >> zagueiro >> goleiro;
    cin >> direcao >> chute;

    if (zagueiro != direcao){
        cout << "Bloqueado" << endl;
    }
    else if (zagueiro == direcao) {

        cout << "Driblado" << endl;

        if (direcao == zagueiro && chute != goleiro){
            cout << "...e o goleiro pega" << endl;

        } else if (direcao == zagueiro && direcao == goleiro) {
            cout << "Gol" << endl;
        }

    }



    return 0;

}