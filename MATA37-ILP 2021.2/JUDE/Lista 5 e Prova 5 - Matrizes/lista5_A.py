pixel_intenso = int(input())

ok = 0
linhas = 10
colunas = 10
matriz = []
for i in range(linhas):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)


for l in range(linhas):
    for c in range(colunas):
        if matriz[l][c] == pixel_intenso:
            ok = 1
            
if ok == 1:
    print("sim")
else:
    print("nao")