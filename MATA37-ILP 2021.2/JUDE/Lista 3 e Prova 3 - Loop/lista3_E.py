E, P =input().split()
E = int(E) 
P = int(P) 
cont = E - P 
contador = 1
contadorP = P - 1
if contadorP > 0:
    while cont > 0:
        cont = cont - contadorP
        contador = contador + 1
        if contadorP <= 0:
            print("F")
            break
        contadorP = contadorP - 1
    else:
        print(contador)
else:
    print("F")