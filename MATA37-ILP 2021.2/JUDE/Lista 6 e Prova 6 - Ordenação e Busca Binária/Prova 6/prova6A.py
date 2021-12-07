clientes = int(input())

lista = [int(x) for x in input().split() ] 


final = len(lista)

for indice in range(1, final):
    posicao = indice
    
    while posicao >= 1 and lista[posicao] < lista[posicao -1]:
        
        guardar = lista[posicao-1]
        lista[posicao -1 ] = lista[posicao]
        lista[posicao] = guardar
        
        posicao -= 1

esq = 0

dir = final -1

meio = (esq + dir) // 2
    


print(lista[meio])