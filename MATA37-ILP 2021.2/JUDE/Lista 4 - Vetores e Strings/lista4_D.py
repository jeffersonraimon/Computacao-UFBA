num_fases = int(input())

pie = 0
boss = 0
fight = 0
ok = 0
for cont in [num_fases]:

    treta = input().split()

life = int(input())
totallife = life


for index, valor in enumerate(treta):

    valor = int(valor)
    
    if valor >= 2:
        life = life - valor
        if life <= 0:
            ok = 1
    if valor == 1:
        life = totallife
if ok == 1:
    print("You Died")
else:
    print("Yes, you can")