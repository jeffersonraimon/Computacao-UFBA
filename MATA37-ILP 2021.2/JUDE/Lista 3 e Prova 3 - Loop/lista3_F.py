n,m = input().split() #n = qtd cinto / m = qtd poções

n = int(n) #n vai ser inteiro e m continuar str

soma = 0 #somador

conjunto = [] # lista 

poderoso = 0 # variavel de controle

for con1 in range(n): # loop baseado na qtd de cinto

    p = input().split() #quantidade do poder das poções
   
    for con2 in p:

        conjunto.append(int(con2)) #joga o valor de con2 na lista de conjuntos

        soma = sum(conjunto) #soma os valores das listas
      
        if soma>poderoso: #se a soma for maior que o poderoso que é = 0

            poderoso=soma

        else:

            poderoso=poderoso 
    conjunto = [] #zera a lista

print(poderoso)