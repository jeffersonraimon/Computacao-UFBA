max = [0]* 1000001
qtd = int(input())
for contador in [qtd]:
    assassinatos = list(map(int, input().split()))

    for contador2 in assassinatos:
        max[contador2] = 1
for i in range(len(max)):
    if max[i] == 1:                
        print(i, end=" ")