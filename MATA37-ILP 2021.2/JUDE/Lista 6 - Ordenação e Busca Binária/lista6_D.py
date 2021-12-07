qtd_pokemon, forma, ordem = input().split()

qtd_pokemon = int(qtd_pokemon)

pokemons = []



for cont in range(qtd_pokemon):
    
    nomepk, nivel = input().split()
    nivel = int(nivel)
    pokemons.append({
        "nome": nomepk,
        "nivel": nivel
    })


if forma == "N": #SE A FORMA FOR POR NIVEL
    

    if ordem == "C":
        for inicio in range(1, qtd_pokemon):
            i = inicio
            while i >= 1 and \
                    (pokemons[i]["nome"] < pokemons[i-1]["nome"]):
                pokemons[i], pokemons[i-1] = pokemons[i-1], pokemons[i]
                i -= 1
        for pk in pokemons:
            print(pk["nome"], pk["nivel"]) 
        
    elif ordem == "D":
        for inicio in range(1, qtd_pokemon):
            i = inicio
            while i >= 1 and \
                    (pokemons[i]["nome"] > pokemons[i-1]["nome"]):
                pokemons[i], pokemons[i-1] = pokemons[i-1], pokemons[i]
                i -= 1
        for pk in pokemons:
            print(pk["nome"], pk["nivel"])


if forma == "L": #SE A FORMA FOR POR LEVEL
    

    if ordem == "C": 
        for inicio in range(1, qtd_pokemon):
            i = inicio
            while i >= 1 and \
                    (pokemons[i]["nivel"] < pokemons[i-1]["nivel"] or
                        (pokemons[i]["nivel"] == pokemons[i-1]["nivel"] and
                        pokemons[i]["nome"] > pokemons[i-1]["nome"])):
                pokemons[i], pokemons[i-1] = pokemons[i-1], pokemons[i]
                i -= 1
        for pk in pokemons:
            print(pk["nome"], pk["nivel"])
        
    elif ordem == "D":    
        for inicio in range(1, qtd_pokemon):
            i = inicio
            while i >= 1 and \
                    (pokemons[i]["nivel"] > pokemons[i-1]["nivel"] or
                        (pokemons[i]["nivel"] == pokemons[i-1]["nivel"] and
                        pokemons[i]["nome"] < pokemons[i-1]["nome"])):
                pokemons[i], pokemons[i-1] = pokemons[i-1], pokemons[i]
                i -= 1
        for pk in pokemons:
            print(pk["nome"], pk["nivel"])