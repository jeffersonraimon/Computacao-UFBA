#N = número com 3 algarismos

#Entrada
Numero = int(input())

Centena = Numero // 100 #resto da div por 100
modCentena = Centena % 10 #descobrir o modulo que vai dizer a centena

Dezena = Numero // 10
modDezena = Dezena % 10

Unidade = Numero // 1
modUnidade = Unidade % 10

#Saida
print(modUnidade, modDezena, modCentena)
