caixaLeiteCond, ovos, caixaLeite , xicAcucar = input().split() #caixas de leite condensado, ovos, litros de leite e xícaras de açúcar

pudean = 1259

caixaLeiteCond = int(caixaLeiteCond)
ovos = int(ovos)
caixaLeite = int(caixaLeite)
xicAcucar = int(xicAcucar)

NovCaixaLeiteCond = caixaLeiteCond // 4
NovOvos = ovos // 8
NovCaixaLeite = caixaLeite // 2
NovAcucar = xicAcucar

if NovCaixaLeiteCond < NovOvos and NovCaixaLeiteCond < NovCaixaLeite and NovCaixaLeiteCond < NovAcucar:

    time = NovCaixaLeiteCond * 1259

    horas = time // 3600
    minutos = (time - (horas* 3600)) //  60
    segundos = time % 60
    print("{} h {} m {} s".format(horas, minutos, segundos))
  #  print(f'{horas}h {minutos}m {segundos}s')

elif NovOvos < NovCaixaLeiteCond and NovOvos < NovCaixaLeite and NovOvos < NovAcucar:

    time = NovOvos * 1259

    horas = time // 3600
    minutos = (time - (horas* 3600)) //  60
    segundos = time % 60
    print("{} h {} m {} s".format(horas, minutos, segundos))
  #  print(f'{horas}h {minutos}m {segundos}s')

elif NovCaixaLeite < NovCaixaLeiteCond and NovCaixaLeite < NovOvos and NovCaixaLeite < NovAcucar:

    time = NovCaixaLeite * 1259

    horas = time // 3600
    minutos = (time - (horas* 3600)) //  60
    segundos = time % 60
    print("{} h {} m {} s".format(horas, minutos, segundos))
  #  print(f'{horas}h {minutos}m {segundos}s')

elif NovAcucar < NovCaixaLeiteCond and NovAcucar < NovOvos and NovAcucar < NovCaixaLeite:

    time = NovAcucar * 1259

    horas = time // 3600
    minutos = (time - (horas* 3600)) //  60
    segundos = time % 60
    print("{} h {} m {} s".format(horas, minutos, segundos))
  #  print(f'{horas}h {minutos}m {segundos}s')