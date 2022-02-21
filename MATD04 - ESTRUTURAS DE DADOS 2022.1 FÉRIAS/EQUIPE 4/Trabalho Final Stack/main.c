#include <stdio.h>
#include <stdlib.h>
#include "functions.h"

void inicializarPilha(Pilha *pilha);
void empilhar(float valor, Pilha *pilha);
void exibir(Pilha *pilha);
void desempilhar(Pilha *pilha);
void limparPilha(Pilha **pilha);

int main() {
    Pilha pilha;
    inicializarPilha(&pilha);
    float novoItem;
    int opcao = 0, controle = 0;

    do {
        system("cls");
        printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
        printf("       C O N T R O L E - C A I X A\n");
        printf("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
        printf("\n");
        printf("1. INSERIR TOTAL DO DIA\n");
        printf("2. IMPRIMIR RELATORIO DIARIO\n");
        printf("3. EXCLUIR ULTIMA ENTRADA\n");
		printf("4. EXCLUIR RELATORIO\n");
        printf("5. SOBRE O PROGRAMA\n");
        printf("6. SAIR DO PROGRAMA\n");
        printf("OPCAO: ");
        scanf(" %d", &opcao);

        switch (opcao) {
            case 1:
                do {
					system("cls");
                    printf("Total de vendas DIA: \n");
                    scanf("%f", &novoItem);
                    empilhar(novoItem, &pilha);
                    printf("Continuar? [1] - S | [2] - N\n");
                    scanf(" %d", &controle);
                } while (controle == 1);
                break;
            case 2:
            	system("cls");
                exibir(&pilha);
                system("pause");
                break;

            case 3:
				system("cls");
                desempilhar(&pilha);
                system("pause");
                break;

            case 4:
				system("cls");
                limparPilha(&pilha);
                inicializarPilha(&pilha);
                printf("RELATORIO EXCLUIDO!!!\n");
                system("pause");
                break;
            case 5:
                system("cls");
                sobre();
                system("pause");
                break;
        }

    } while (opcao != 6);
    return 0;
}