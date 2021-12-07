meio = -1
feiticos = []

geral = int(input()) 

for cada in [geral]:
    feit_gerais = input().split() 

    
proibido = int(input()) 

for cada2 in [proibido]:
    feits_proib = input().split() 
    

comparar = int(input()) 

for cada3 in [comparar]:
    feits = input().split() 
    
    for i in range(comparar):
        f = feits[i]

    
        n = len(feit_gerais)
        esq = 0
        dir = n - 1
        
        while esq <= dir:
            
            meio = (esq + dir) // 2
            
            if feit_gerais[meio] == f:
                break
            elif f < feit_gerais[meio]:
                
                dir = meio - 1
            else:
                esq = meio + 1
                
        if feit_gerais[meio] == f:
            print("Geral")
        else:
            print("Proibido")