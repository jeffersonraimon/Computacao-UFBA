A,B = map(int,input().split())
X = []
Y = []
Z = []
for i in range(A):
  C,D = map(int,input().split())
  X.append((C,D))
  Y.append(D)
X = sorted(X)
 
for j,valor in enumerate(X):
 x = valor[1]
 Z.append(x)
if Z == Y:
  print("Y")
else:
  print("N")