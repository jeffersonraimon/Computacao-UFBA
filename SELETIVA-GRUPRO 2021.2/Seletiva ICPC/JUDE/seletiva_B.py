palavra = input()

if len(palavra) > 10:
   compr = palavra

   print(compr[0],len(compr[2:]),compr[-1], sep="")
else:
    print(palavra)