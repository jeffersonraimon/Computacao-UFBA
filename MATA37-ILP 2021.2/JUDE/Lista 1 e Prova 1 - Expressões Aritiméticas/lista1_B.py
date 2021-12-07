#Entradas
#A - total de naves INIMIGAS no quadrante
#B - total de naves AMIGAS na frente
#C - total de naves AMIGAS na direita
#D - total de naves AMIGAS na esquerda
#E - total de naves AMIGAS atrás

A, B, C, D, E = input().split()


tNavesA = int(B) + int(C) + int(D) + int(E) #total de naves amigas

tNavesI = int(A) - tNavesA #total de naves inimigas

#Saida
print(tNavesI) 