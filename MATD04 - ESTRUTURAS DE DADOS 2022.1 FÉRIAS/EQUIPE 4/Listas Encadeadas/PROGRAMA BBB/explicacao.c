#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct no No;
struct no{

    char *pessoa;
    struct no *prox;
};


No* criar_no(){
    No* novo = (No*)malloc(sizeof(No));
    return novo;
}

No* inserir_no_inicio(No* Lista, char* nome){
    No* novo_no = criar_no();
    novo_no->pessoa = nome;
    
    if (Lista == NULL){
        Lista = novo_no;
        novo_no -> prox = NULL;
    } else {
        novo_no -> prox = Lista;
        Lista = novo_no;
    }
    return Lista;
}

void imprimir_lista(No* Lista){

    No *aux = Lista;

    while (aux != NULL){
        printf("%s\n", aux->pessoa);
        aux = aux->prox;
    }

}

int main (){
  
  No *Lista = NULL;
  
  Lista = inserir_no_inicio(Lista, "jefferson");
  Lista = inserir_no_inicio(Lista, "rafael");
  Lista = inserir_no_inicio(Lista, "winny");
  
  imprimir_lista(Lista);
  
 return 0; 
}  
  
