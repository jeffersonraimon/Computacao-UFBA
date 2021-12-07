tamanho = int(input())

linhas = tamanho

somadorH = 0
somadorR = 0

matriz = [[int(x) for x in input().split()] for i in range(tamanho)]

harry, ron = [int(z) for z in input().split()]



for j in range(linhas):
    somadorR = somadorR + matriz[j][ron]
    matriz[j][ron] = 0
    somadorH = somadorH + matriz[harry][j]
    matriz[harry][j] = 0
    
    
print("Harry",somadorH)
print("Ron", somadorR)

