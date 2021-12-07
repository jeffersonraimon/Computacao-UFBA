ovos_coletados = 0

ovos_total = 0



linhas, colunas = [int(x) for x in input().split()]

matriz = [[int(z) for z in input().split()] for i in range(linhas)]


for l in range(linhas):
    
    if l % 2 == 0:
    
        for c in range(colunas):
            ovos_coletados = ovos_coletados + matriz[l][c]
            if ovos_coletados < 0:
                ovos_coletados = 0
    else:
        for c in range(colunas-1, -1,-1):
            #ovos_coletadosD = ovos_coletadosD + matriz[l][c]
            ovos_coletados = ovos_coletados + matriz[l][c]
            if ovos_coletados < 0:
                ovos_coletados = 0
ovos_total = ovos_coletados      
print(ovos_total)