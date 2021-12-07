c = int(input())

contador = 0
contador2 = 0

for cont in range(c):

    tempoLimite, qtdMortes, qtdHorasMissoes = input().split()
   
    tempoLimite = int(tempoLimite)
    qtdMortes = int(qtdMortes)
    qtdHorasMissoes = int(qtdHorasMissoes)

    total = tempoLimite * qtdMortes
    
    contador = total + contador
    contador2 = qtdHorasMissoes + contador2
soma = (contador + contador2)
print(soma)