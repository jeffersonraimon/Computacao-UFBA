somadorA = 0
somadorB = 0
somadorC = 0
somadorD = 0
desnivel_A = 0
desnivel_B = 0
desnivel_C = 0
desnivel_D = 0

linhas, colunas = [int(z) for z in input().split()]

matriz = []
for z in range(linhas):
   linha = [int(x) for x in input().split()]
   matriz.append(linha)

lin, col = [int(z) for z in input().split()]

topo = matriz[lin][col]


for j in range(colunas):
    somadorA = somadorA + matriz[0][j]
    somadorC = somadorC + matriz[linhas-1][j]

for i in range(linhas):
    somadorB = somadorB + matriz[i][colunas-1]
    somadorD = somadorD + matriz[i][0]
        
    


desnivel_A = topo - (somadorA / colunas) 
desnivel_B = topo - (somadorB / linhas) 
desnivel_C = topo - (somadorC / colunas) 
desnivel_D = topo - (somadorD / linhas) 


if desnivel_A > desnivel_B and desnivel_A  > desnivel_C and desnivel_A > desnivel_D:
    print("Lado A")
elif desnivel_B > desnivel_A and desnivel_B  > desnivel_C and desnivel_B > desnivel_D:
    print("Lado B")
elif desnivel_C > desnivel_A and desnivel_C  > desnivel_B and desnivel_C > desnivel_D:
    print("Lado C")
elif desnivel_D > desnivel_A and desnivel_D  > desnivel_B and desnivel_D > desnivel_C:
    print("Lado D")
