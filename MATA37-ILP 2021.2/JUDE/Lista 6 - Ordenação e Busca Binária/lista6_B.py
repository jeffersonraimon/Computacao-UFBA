dançarinos = int(input())

for cont in [dançarinos]:
    homens = [int(x) for x in input().split()]

for cont in [dançarinos]:
    mulheres = [int(x) for x in input().split()]

#n = len(v)

for inicio in range(1, dançarinos):
    i = inicio
    while i >= 1 and homens[i] > homens[i-1]:
        homens[i], homens[i-1] = homens[i-1], homens[i]
        i -= 1

for inicio in range(1, dançarinos):
    i = inicio
    while i >= 1 and mulheres[i] < mulheres[i-1]:
        mulheres[i], mulheres[i-1] = mulheres[i-1], mulheres[i]
        i -= 1        

for idade in range(dançarinos):
    print(homens[idade], mulheres[idade])