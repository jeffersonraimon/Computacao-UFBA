#include "lista.h"
void cabecalhoBBB();
No* criar_no();
No* inserir_no_inicio(No* Lista, char* nome);
void imprimir_lista(No* Lista);

void brother(){
    
int Resposta = 0;
while (Resposta == 0){

    string brother = get_string("Digite o nome do brother: ");

    if (strcmp(brother, "parar") == 0){
        Resposta = 1;
    } else {
        Lista = inserir_no_inicio(Lista, brother);
    }

}

}

