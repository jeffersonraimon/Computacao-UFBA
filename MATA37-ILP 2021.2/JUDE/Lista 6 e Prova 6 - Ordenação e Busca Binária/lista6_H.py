"""def pesquisa_binaria(A, item):
    somador = 0
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] <= item:
            somador = somador + 1
            A[meio] = 0
            return somador
        elif A[meio] > item:
            direita = meio - 1
        else: 
            esquerda = meio + 1
    return -1


a = dict(enumerate([0]*1000, 1))


lista = []
lista2 = []

largura, comprimento = map(int, input().split())

matriz = [[int(x) for x in input(). split()] for i in range(largura)]

horas = int(input())

instantes = [int(z) for z in input().split()]


for inicio in range(largura):
        for inicio2 in range(comprimento):
            lista.append(int(matriz[inicio][inicio2]))

lista.sort()



for cada in range(len(instantes)):
    f = instantes[cada]

    
    
    for cada_elemento in range(len(lista)):
        
        if lista[cada_elemento] <= f:
            
            lista2.append(lista[cada_elemento])
            

    print(len(lista2))
    lista2 = []"""
    

"""
def pesquisa_binaria(A, item):
    somador = 0
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] <= item:
            somador = somador + 1
            A[meio] = 0
            return somador
        elif A[meio] > item:
            direita = meio - 1
        else: 
            esquerda = meio + 1
    return -1
"""


a = dict(enumerate([0]*1000, 1))



largura, comprimento = map(int, input().split())



for i in range(largura):
    for x in input().split():
	    a[int(x)] += 1


horas = int(input())

instantes = [int(z) for z in input().split()]

va = list(a.values())

for inst in instantes:
    soma = 0
    soma = sum(va[:inst])
    print(soma)