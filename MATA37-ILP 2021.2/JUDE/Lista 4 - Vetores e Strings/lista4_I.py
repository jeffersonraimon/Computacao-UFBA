st = str(input()).replace(" ","").lower()
lista = []
for indice, p in enumerate(st):
    lista.append(p)
    teste = lista[::-1]
if lista == teste:
    print("Palindromo")
else:
    print("!Palindromo")
