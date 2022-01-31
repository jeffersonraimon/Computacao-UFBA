#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include "cabecalhoBBB.h"
#include "lista.h"

void cabecalhoBBB();
No* criar_no();
No* inserir_no_inicio(No* Lista, char* nome);
void imprimir_lista(No* Lista);


int main(){


    No *Lista = NULL;

    int programa = 0;


    do {

    system("clear");
    cabecalhoBBB();
    
    int resposta = get_int("Sua Opção: ");

    if (resposta < 0 || resposta > 4){
        printf("Opção Inválida!!!\n");
    } else{

    if (resposta == 1) { //[1] - Inserir brother

        int Resposta = 0;
        while (Resposta == 0){

            string brother = get_string("Digite o nome do brother! ['q'] - termina de adicionar: ");

        if (strcmp(brother, "q") == 0){
                Resposta = 1;
                system("clear");
        } else {
                Lista = inserir_no_inicio(Lista, brother);
        }

        }

        }
    if (resposta == 2){ //2] - Imprimir brothers

            char resp = 'n';

            if (Lista == NULL){

                printf("a lista está vazia :( \n");

                do {

                    resp = get_char("Digite 'q' para voltar ao inicio! :");

                    system("clear");

                } while( resp == 'n');


            } else {
                printf("\n");
                system("clear");
                printf("Brothers no Paredão! - [Do mais recente ao mais antigo]\n");
                printf("\n");
                imprimir_lista(Lista);
                printf("\n");
                do {
                    resp = get_char("Digite 'q' para voltar ao inicio! ");
                    system("clear");
                } while( resp == 'n');

            }

        }
    if (resposta == 3){ //3] - Sair do programa

        programa = resposta;
        system("clear");
    }

    }
    } while (programa == 0);

    return 0;

}