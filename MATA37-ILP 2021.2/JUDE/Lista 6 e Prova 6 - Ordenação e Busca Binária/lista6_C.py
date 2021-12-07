n = int(input())

teste = []

for cont in range(n):
    idd, urgencia = map(int, input().split()) 
    teste.append({
        "id": idd,
        "urgencia": urgencia
    })

for inicio in range(1, n):
   i = inicio
   while i >= 1 and \
           (
               teste[i]["urgencia"] > teste[i-1]["urgencia"]):
       teste[i], teste[i-1] = teste[i-1], teste[i]
       i -= 1

for priori in teste:
   print(priori["id"], priori["urgencia"])
