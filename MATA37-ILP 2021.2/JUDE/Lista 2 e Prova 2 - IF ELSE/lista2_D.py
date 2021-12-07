direcZag, direcGo = input().split() #direção zagueiro defesa / direção goleiro defesa
direcAtac, direcChut = input().split() #direção atacante dibre / direção chute


if direcZag != direcAtac:
    print("Bloqueado\n")
elif direcZag == direcAtac:
    print("Driblado")
    if direcAtac == direcZag and direcChut != direcGo:
        print('...e o goleiro pega')
    elif direcAtac == direcZag and direcChut == direcGo:
        print('Gol')