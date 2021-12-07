linhas, colunas = [int(z) for z in input().split()]

ok = 0

matriz = []
for i in range(linhas):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)


for l in range(linhas):
    for c in range(colunas):
        if matriz[l][c] == 0:
            if matriz[l-1][c] == 1 and matriz[l+1][c] == 1 and matriz[l][c-1] == 1 and matriz[l][c+1] == 1:
                print(l, c)
            else:
                print("0 0")
