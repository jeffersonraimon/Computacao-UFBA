n, x, xpmin = input().split()

n = int(n)
x = int(x)
xpmin = int(xpmin)

for i in range(n):
    xpatual, qtdmissoes = input().split()

    xpatual = int(xpatual)
    qtdmissoes = int(qtdmissoes)
    
    if xpatual < xpmin:
        print(xpatual, qtdmissoes)
    else:
        print((xpatual+x), (qtdmissoes+1))