tamanho, teleportes = input().split()
tamanho = int(tamanho)
teleportes = int(teleportes)

nave = False
ok = 0

matriz = [[int(x) for x in input().split()] for i in range(tamanho)]


for _ in range(teleportes):
    posicaoL, posicaoC = map(int, input().split())
       
    nave = False
    
    for l in range(posicaoL-1,-1,-1):
        
        if matriz[l][posicaoC] == 1:
            nave = True
            matriz[l][posicaoC] = 0
            break
    
    if nave == True:
        ok = ok + 1
print(ok)