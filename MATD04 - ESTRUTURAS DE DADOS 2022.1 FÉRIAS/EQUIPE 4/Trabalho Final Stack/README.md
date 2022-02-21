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

![programa](https://user-images.githubusercontent.com/80064475/154977517-f8a852d9-9433-4cd0-8688-c5d205201373.png)

## Por quê pilha?

Nas atividades diárias de um mercado, é necessário haver um controle de caixa, em que se possa inserir o valor total do caixa a cada dia. Assim, criamos um programa em que se pode inserir o valor total do caixa por dia e remover apenas o último no caso de erro, o que faz a estrutura de pilha a ideal devido ser do tipo LIFO (last in, first out) e possibilita atender essa necessidade do programa.

Os dias que passaram acabarão sendo empilhados e no relatório será mostrado do primeiro dia ao último, de baixo pra cima.

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

Para o *struct* usamos duas estruturas:

- uma estrutura *NO* (utilizamos o typedef para facilitar a organização e entendimento do código) com dois elementos, uma valor *float* e um ponteiro para outro nó.

- e a estrutura *PILHA*, que possui um elemento do tipo **NO* chamado topo, e um tamanho *int* para o tamanho da pilha.

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

### Inicializar Pilha

```c
void inicializarPilha(Pilha *pilha) {
  pilha->topo    = NULL;
  pilha->tamanho = 0;
}
```

Essa função fica responsável de inicializar a estrutura pilha da seguinte forma:

- recebe como argumento um ponteiro do tipo Pilha (definido na Struct). 

- acessa a struct e define o valor do ponteiro topo como NULL e o tamanho da pilha como 0.

### Empilhar

```c
void empilhar(float valor, Pilha *pilha) {
  No *novoNo = malloc(sizeof(No));
  novoNo->valor = valor;
  if (pilha->tamanho == 0)
    novoNo->proximo = NULL;
  else
    novoNo->proximo = pilha->topo;
  pilha->topo = novoNo;
  pilha->tamanho++;
}
```

Para a operação de empilhar:

- recebe como parâmetro um ponteiro do tipo *Pilha* para a nossa pilha e o elemento do tipo *float*a ser inserido.

- um novo nó é alocado dinamicamente e inserido no topo da pilha.

- atualizamos o ponteiro para o topo.

- acessamos o parâmetro tamanho e incrementamos ele.

### Exibir Pilha

```c
void exibir(Pilha *pilha) {
  No *temporario;
  float soma = 0;
  temporario = pilha->topo;
  int i = pilha->tamanho;
  while (i > 0) {
    soma += temporario ->valor;
    printf("Dia: %i | Valor: [ R$%5.2f ]\n", i, temporario->valor);
    temporario = temporario->proximo;
    i--;
  }
```

### Desempilhar

```c
void desempilhar(Pilha *pilha) {
  if (pilha->tamanho == 0) {
    printf("Sem Relatorios\n");
  } else {
    printf(" VALOR: [R$%5.2f] EXCLUIDO\n", pilha->topo->valor);
    pilha->tamanho--;
    pilha->topo = pilha->topo->proximo;
  }
}
```

Para a operação de desempilhar:

- retorna o ponteiro para o topo desempilhado ou nulo caso a pilha esteja vazia.

- antes de retornar ao nó desempilhado, o topo é atualizado para o nó seguinte.
