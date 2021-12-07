L, C = [int(x) for x in input().split()]
matrizA = []
matrizB = []
matrizC = []
matrizD = []
result = 0
matrizA = [[int(xA) for xA in input().split()] for iA in range(L)]
matrizB = [[int(xB) for xB in input().split()] for iB in range(L)]

for l in range(L):
   for c in range(C):
       matrizC = matrizA[l][c]
       matrizD = matrizB[l][c]
       result = matrizC - matrizD      
       #print(matrizB[l][c], end=" ")
       print(result, end =" ")
   print()
