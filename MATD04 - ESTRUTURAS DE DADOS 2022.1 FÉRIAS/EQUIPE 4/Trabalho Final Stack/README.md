# TRABALHO FINAL | CONTROLE DE CAIXA



```
Universidade Federal da Bahia - UFBA

Instituto de Computação

MATD04 - Estruturas de Dados | 2022.1 - Férias

Equipe: 04 - Heron Oliveira, Lílian Sousa, Jefferson Raimon, João Abreu, Mateus Moura, Rafael Casaes, Wanderson Santos.

Professora: Cristiana Bispo
```



## Introdução

Neste trabalho, nós desenvolvemos um programa que recebe como valor de entrada o  saldo total do caixa no dia, de um supermecado e o armazena numa estrutura de dados do tipo pilha. Também é possível imprimir o relatório dos valores de cada dia, excluir a ultima entrada e também excluir todo o relatório.

## Estrutura da Pilha

```c

typedef struct NO{
  float valor;
  struct NO *proximo;
} No;

typedef struct PILHA{
  No *topo;
  float tamanho;
} Pilha;
```

## Funções da Pilha

```c
void inicializarPilha(Pilha *pilha);
```

```c
void empilhar(float valor, Pilha *pilha);
```

```c
void exibir(Pilha *pilha);
```

```c
void desempilhar(Pilha *pilha);
```

```c
void limparPilha(Pilha **pilha);
```

## Inicializar Pilha

```c
void inicializarPilha(Pilha *pilha) {
  pilha->topo    = NULL;
  pilha->tamanho = 0;
}
```

Essa função fica responsável de inicializar a estrutura pilha da seguinte forma: acessa a struct e define o valor do ponteiro topo como NULL e o tamanho da pilha como 0.


