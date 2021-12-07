homens = 0
mulheres = 0

n = int(input())

for cont in range(n):
    s = int(input())

    if s == 1:
        homens = homens + 1
    else:
        mulheres = mulheres + 1
print(homens)
print(mulheres)
