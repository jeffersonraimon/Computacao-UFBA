#include <iostream>

using namespace std;

int main(){

    int caçada1 = 0, caçada2 = 0, caçada3 = 0;
    int ovosEnv1 = 0, ovosEnv2 = 0, ovosEnv3 = 0;
    int total = 0, ovosEnv;

    cin >> caçada1 >> caçada2 >> caçada3;
    cin >> ovosEnv1 >> ovosEnv2 >> ovosEnv3;

    ovosEnv = (ovosEnv1 + ovosEnv2 + ovosEnv3) * 3;

    total = (caçada1 + caçada2 + caçada3) - ovosEnv;

    cout << total;

    return 0;

}
