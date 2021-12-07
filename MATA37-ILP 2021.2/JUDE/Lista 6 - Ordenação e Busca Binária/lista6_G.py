def pesquisa_binaria(A, item):
    #somador = 0
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else: 
            esquerda = meio + 1
    return -1


qtd_planetas = int(input()) 


planetasGeral = input().split()

yodaVerificar = int(input()) 


planetasYoda = input().split()
    

matriz = [[int(x) for x in input().split()] for i in range(qtd_planetas)]


planetasIndex ={p:pesquisa_binaria(planetasGeral, p) for p in planetasYoda}

somador = matriz[0][planetasIndex[planetasYoda[0]]]

for x in range(1, len(planetasYoda)):
    antIndex = planetasYoda[x-1]
    agrIndex = planetasYoda[x]
    
    anterior = planetasIndex[antIndex]
    agora = planetasIndex[agrIndex]
    
    somador += matriz[anterior][agora]

print(somador)
