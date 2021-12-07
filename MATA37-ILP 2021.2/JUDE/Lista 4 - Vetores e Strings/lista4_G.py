s = str(input()).replace(" ","")
q, p = input().split()
q = int(q)
p = str(p)


teste = s.count(p)

print(teste)

if teste == q: 
    print("SIM!")
else:
    print("NAO!")
