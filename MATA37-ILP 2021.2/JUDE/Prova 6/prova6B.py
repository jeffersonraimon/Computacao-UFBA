def buscabin(lista, item):
    somador0 = 0
    esquerda = 0
    direita = len(lista) -1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio -1
        else:
            esquerda = meio + 1
    return 0


totaldims, mortydims=[int(f) for f in input().split()]

listaDims = [int(x) for x in input().split()]

dimens = [int(x) for x in input().split()]

somador = 0

for i in range (mortydims):
    
    esquerda = 0
    direita = totaldims - 1

    while esquerda <= direita:
        
        meio = (esquerda + direita) // 2
        
        if listaDims[meio] == dimens[i]:
            
            break
        
        elif dimens[i] < listaDims[meio]:
            
            direita = meio - 1
            
        elif dimens[i]>listaDims[meio]:
            
            esquerda = meio + 1
            
    if listaDims[meio] == dimens[i]:
        
        somador+=1

print(somador)


"""
    def buscabin(lista, item):
        somador = 0
    esquerda = 0
    direita = len(lista) -1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return "ok"
        elif lista[meio] > item:
            direita = meio -1
        else:
            esquerda = meio + 1
    return 0
    

totaldims, mortydims = [int(f) for f in input().split()]

listaDims = [int(x) for x in input().split()]

dimens = [int(z) for z in input().split()]

somador2 = 0

teste = {p:buscabin(listaDims, p) for p in dimens}


for num in teste:
    
    if teste[num] == "ok": 
        somador2 += 1

print(somador2)
    
"""