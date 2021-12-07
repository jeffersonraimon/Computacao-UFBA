num_nomes = int(input())

for cont in range(num_nomes):
    nomeC = input().split()
    nome2=[0]*len(nomeC)
    

    for cont2, nome3 in enumerate(nomeC):
        nome2[cont2]=nome3[0].capitalize()+"."
    numNomes = len(nomeC)
    numNomes = -1

    nome2[numNomes] = nomeC[numNomes].title()

    print(*nome2)