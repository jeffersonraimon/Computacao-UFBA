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

