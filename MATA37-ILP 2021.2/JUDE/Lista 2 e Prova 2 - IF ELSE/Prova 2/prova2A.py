dr, gu, ar, dt = input().split()
cb = int(input())

dr = int(dr)
gu = int(gu)
ar = int(ar) 
dt = int(dt) 

dr = dr* 5000
gu = gu * 20
ar = ar * 25
dt = dt * 25

aliados = dr + gu + ar + dt

if aliados >= cb:
    print("VITORIA")
else:
    print("DERROTA")