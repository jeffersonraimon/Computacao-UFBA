#include <iostream>

using namespace std;

int main(){


    int x = 0, y = 0;

    cin >> x;
    cin >> y;

    if (x > 0 && y > 0){
        //
        cout << "Quadrante 1";
    } else if ( x < 0 && y > 0){
        //
        cout << "Quadrante 2";
    } else if (x < 0 && y < 0){
        //
        cout << "Quadrante 3";
    } else if (x > 0 && y < 0){
        //
        cout << "Quadrante 4";
    } else{
        cout << "Centro";
    }


    return 0;

}