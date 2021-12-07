a, b, c = input().split()

a = int(a) #quantidade de pistas
b = int(b) #quantidade de pessoas por pista
c = int(c) #quantidade de alunos



qtd = a * b

if qtd > c:
    print('S')
else:
    print('N')