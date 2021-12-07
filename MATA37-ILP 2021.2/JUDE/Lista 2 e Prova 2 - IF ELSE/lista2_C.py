x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('Quadrante 1\n')
elif x < 0 and y > 0:
    print('Quadrante 2\n')

elif x < 0 and y < 0:
    print('Quadrante 3\n')
elif x > 0 and y < 0:
    print('Quadrante 4\n')
else:
    print('Centro')