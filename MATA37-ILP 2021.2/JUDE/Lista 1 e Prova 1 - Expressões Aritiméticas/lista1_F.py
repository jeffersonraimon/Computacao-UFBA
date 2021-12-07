#1 hora tem 3600s
#1 minuto tem 60s

#Entrada
tempoSeg = int(input()) #tempo inserido em segundos

hora = tempoSeg // 3600 #descobrir a hora
minuto = (tempoSeg - (hora * 3600)) // 60 #quantidade de hora menos o total em segundos dividido por 60 
segundo = tempoSeg % 60 #segundos

#Saida
print("{}h {}m {}s" .format(hora,minuto,segundo)) 