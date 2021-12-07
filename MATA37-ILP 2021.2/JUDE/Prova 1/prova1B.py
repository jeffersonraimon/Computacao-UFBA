qOvos1, qOvos2, qOvos3 = input().split()

qOvos1 = int(qOvos1)
qOvos2 = int(qOvos2)
qOvos3 = int(qOvos3)

qOvosE1, qOvosE2, qOvosE3 = input().split()

qOvosE1 = int(qOvosE1)
qOvosE2 = int(qOvosE2)
qOvosE3 = int(qOvosE3)

ovosEnv = (qOvosE1 + qOvosE2 + qOvosE3) * 3
totalOvos = (qOvos1 + qOvos2 + qOvos3) - ovosEnv

print(totalOvos)