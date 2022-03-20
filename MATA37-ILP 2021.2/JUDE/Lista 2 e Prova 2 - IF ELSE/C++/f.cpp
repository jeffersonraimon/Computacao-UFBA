#include <iostream>

using namespace std;

int main(){

    int N1, N2, N3, N4, N5, N6;
    int soma;

    cin >> N1 >> N2 >> N3 >> N4 >> N5 >> N6;

    soma = N1 + N2 + N3 + N4 + N5 + N6;

    if (soma >= 250){
        cout << "S+" << endl;
    } else if (soma >= 200){
        cout << "S" << endl;
    } else if (soma >= 180){
        cout << "S-" << endl;
    } else if (soma >= 150){
        cout << "A+" << endl;
    } else if (soma >= 100){
        cout << "A" << endl;
    } else if (soma >= 80){
        cout << "A-" << endl;
    } else if (soma >= 60){
        cout << "B+" << endl;
    } else if (soma >= 40){
        cout << "B" << endl;
    } else if (soma >= 39){
        cout << "B-" << endl;
    }



    return 0;

}