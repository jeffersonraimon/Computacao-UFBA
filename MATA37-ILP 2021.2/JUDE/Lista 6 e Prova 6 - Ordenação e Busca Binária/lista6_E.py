num_catalogo_especie = int(input())


especies = []
especies2 = []

for cada in range(num_catalogo_especie):
    especie = input()
    especies.append(especie)
    
num_especies_para_pesquisar = int(input())

for cada2 in range(num_especies_para_pesquisar):
    especie2 = input()
    #especies2.append(especie2)
    
    n = len(especies)
    esq = 0
    dir = n - 1
    
    while esq <= dir:
        meio = (esq + dir) // 2
        if especies[meio] == especie2:
            break
        elif especie2 < especies[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
            
    if especies[meio] == especie2:
        print(especies[meio], "vive!")
    else:
        print(especie2, "foi extinto :(")