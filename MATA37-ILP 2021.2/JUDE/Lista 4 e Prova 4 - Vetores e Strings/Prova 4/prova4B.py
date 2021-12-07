N, M = map(int, input().split())

zero = 0

L = list(map(int, input().split()))

while zero in L:

    L.remove(0)

L1 = L[::-1]
L1 = L1[0:M]
L1.reverse()

print(*L1)