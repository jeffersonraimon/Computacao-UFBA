n1, n2, n3, n4, n5, n6 = input().split()

n1  = int(n1)
n2  = int(n2)
n3  = int(n3)
n4  = int(n4)
n5  = int(n5)
n6  = int(n6)

maestria = n1 + n2 + n3 + n4 + n5 + n6

if maestria >= 250:
    print('S+')
elif maestria >= 200 and maestria <= 249:
    print('S')
elif maestria >= 180 and maestria <= 199:
    print('S-')
elif maestria >= 150 and maestria <= 179:
    print('A+')
elif maestria >= 100 and maestria <= 149:
    print("A")
elif maestria >= 80 and maestria <= 99:
    print("A-")
elif maestria >= 60 and maestria <= 79:
    print("B+")
elif maestria >= 40 and maestria <= 59:
    print("B")
elif maestria <= 39:
    print("B-")