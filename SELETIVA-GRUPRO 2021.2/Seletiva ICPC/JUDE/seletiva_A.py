t = int(input())

for cont in range(t):

    si = input()

    teste = si[4]
    
    if not teste.isdigit():

        print("Novo")
        
    else:
        print("Antigo")