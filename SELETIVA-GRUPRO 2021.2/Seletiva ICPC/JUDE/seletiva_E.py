def isitPrime(k): #essa funcao tive que pegar na net kkk
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

n = int(input())

par = 0

impar = 0

primo = 0

for cont in [n]:

    teste = input().split()

    for cont2 in teste:

        cont2 = int(cont2)

        if cont2 % 2 == 0:

            par = par + 1
        if isitPrime(cont2) == True:

            primo = primo + 1    

        if cont2 % 2 != 0:

            impar = impar + 1
        
print(par, "valor(es) par(es)")

print(impar, "valor(es) impar(es)")

print(primo, "valor(es) primo(s)")