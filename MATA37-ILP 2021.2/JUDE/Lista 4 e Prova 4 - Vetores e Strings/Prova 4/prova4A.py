qtd_config = int(input())

valoresCod = list(map(int,input().split()))

pvalores = int(input())

somador = 0

for indice,valores in enumerate(valoresCod):

    if indice < pvalores:

        somador=somador+valores

if somador % 2 != 0:

    print ('SERN')
else:
    print ('tutturu')