frase = str (input ("digite uma frase :")).upper().strip()
print ("A letra A aparece {} vezes na frase".format(frase.count ("A")))
print ("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
print("A ultima vez que a letra A apareceu, foi na posição {}".format(frase.rfind("A")))