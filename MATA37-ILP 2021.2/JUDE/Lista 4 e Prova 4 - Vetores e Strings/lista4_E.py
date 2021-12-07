sapos, pedras = input().split()

sapos = int(sapos)
pedras = int(pedras)
ppedras = [0]*pedras

for contador in range(sapos):
    pulo = int(input())

    for contador2 in range(0,pedras,pulo):
        ppedras[contador2] = 1
        
print(*ppedras)