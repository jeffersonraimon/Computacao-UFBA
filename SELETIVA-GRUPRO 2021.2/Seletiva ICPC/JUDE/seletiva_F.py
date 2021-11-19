import collections

n = int(input())
teste1 = 0
for cont in [n]:
    antesAcid = input().split()
    depoisAcid = input().split()
    
    if (collections.Counter(antesAcid)==collections.Counter(depoisAcid)):
        teste1 = 1
    else:
        teste1 = 2
if teste1 == 1:
    print("Intacta")
else:
    print("Alterada")