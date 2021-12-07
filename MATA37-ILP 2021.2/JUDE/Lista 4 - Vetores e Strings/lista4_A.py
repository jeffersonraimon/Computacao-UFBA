num_itens = int(input())
#itens = map(int, input().split())
itens = [int(x) for x in input().split()]
itens.reverse()
print(*itens)