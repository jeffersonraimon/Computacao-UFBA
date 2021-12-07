linha = 10
coluna = 10


matriz = [[str(x) for x in input().split()] for i in range(linha)]

for l in range(linha):
    
    for c in range(coluna):

    
        if l-1 >= 0:
            if matriz[l-1][c]=='*' and matriz[l][c]=='t':
                matriz[l][c]='p'
        if c-1 >= 0:
            if matriz[l][c-1]=='*' and matriz[l][c]=='t':
                matriz[l][c]='p'
        if l+1 < linha:
            if matriz[l+1][c]=='*' and matriz[l][c]=='t':
                matriz[l][c]='p'
        if c+1 < linha:
            if matriz[l][c+1]=='*' and matriz[l][c]=='t':
                matriz[l][c]='p'

for c1 in range(linha):
   for c2 in range(coluna):
       print(matriz[c1][c2], end=" ")
   print()