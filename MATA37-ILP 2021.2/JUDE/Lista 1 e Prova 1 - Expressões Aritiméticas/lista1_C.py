#K = Kanto, Kreg = pokemons registrados de Kanto, Knew = novos pokemons capturados em Kanto
#J= Johto, Jreg = pokemons registrados de Johto, Jnew = novos pokemons capturados em Johto
#H = Hoenn, Hreg = pokemons registrados de Hoenn, Hnew = novos pokemons capturados em Hoenn



#Entrada

Kreg, Jreg, Hreg = input().split()
Knew, Jnew, Hnew = input().split()

tK = int(Kreg) + int(Knew) #total pokemons de Kanto
tJ = int(Jreg) + int(Jnew) #total pokemons de Johto
tH = int(Hreg) + int(Hnew) #total pokemons de Hoenn

#Saida
print(tK,"",tJ,"",tH)
print("") #quebra de linha
