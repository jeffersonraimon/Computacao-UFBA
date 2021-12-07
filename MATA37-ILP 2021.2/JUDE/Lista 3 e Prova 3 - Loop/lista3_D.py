T = int(input())

P = int(input())

controle = 0 #Uso para guardar o valor maior que o limite

while P != 0:

    P = int(input())

    if P >= T:

        controle = 1 #coloquei 1 so pra ser diferente de 0

if controle == 1:

    print("ALARME")

else:

    print("O Havai pode dormir tranquilo")