frase = str(input("digite uma frase :")).strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letras in range(len(junto)- 1, -1, -1):
     inverso += junto [letras]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("\033[32m A frase digita é palídromo !")
else:
    print(" \n\033[31m A frase digitada não é  palídromo !")



   