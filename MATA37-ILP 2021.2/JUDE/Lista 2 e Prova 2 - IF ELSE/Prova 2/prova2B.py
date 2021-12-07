
fenoComprar,fenoDisp = input().split()
fenoComprar = int(fenoComprar)
fenoDisp = int(fenoDisp)
total = fenoDisp - fenoComprar
total = total % 2
if fenoDisp > fenoComprar:
    if total == 0:
        print('vendido')
    else:
        print('sinto muito')
else:
    print('sinto muito')