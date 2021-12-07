jogadores = int(input())

for cont in [jogadores]:
    v = [int(x) for x in input().split()]

for inicio in range(1, jogadores):
    i = inicio
    while i >= 1 and v[i] < v[i-1]:
        v[i], v[i-1] = v[i-1], v[i]
        i -= 1
print(*v[:8])