xE, yE = input().split()
xE = int(xE)
yE = int(yE)
xD, yD = input().split()
xD = int(xD)
yD = int(yD)


entrega = xE + yE

destino = xD + yD

if entrega == destino:

    print('Soltar pacote')
else:

    print("Nao soltar pacote")