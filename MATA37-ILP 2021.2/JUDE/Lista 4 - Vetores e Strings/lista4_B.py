num_caixas = int(input())
num_esmeraldas = [int(x) for x in input().split()]
esmeralda = int(input())
lista = [esmeralda]
if set(num_esmeraldas) & set(lista):
    print(esmeralda)
else:
    print(-1)
