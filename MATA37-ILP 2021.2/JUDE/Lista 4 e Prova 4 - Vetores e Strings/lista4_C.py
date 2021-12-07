n = int(input())
comp = [int(x) for x in input().split()]

total_dividido = (sum(comp)) // 2


somadorIndice = 0
SomadorValor=0
teste = 0
teste2 = 0



for indice, valor in enumerate(comp):

    SomadorValor = SomadorValor + valor
    somadorIndice = indice

    if SomadorValor == total_dividido:

        teste = valor
        teste2 = somadorIndice
        break

print(teste2+1)