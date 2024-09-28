from random import choice
from time import sleep
digite = int(input("digite um numero entre 1-4 :"))
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5 

lista = [n1, n2, n3, n4, n5]
sorteio = choice(lista)
 
print("o numero sorteado foi {}".format(sorteio))

if digite == sorteio:
     print("parabens vc venceu")
   
else: print("ops não foi desta vez")

if digite < 1 or digite > 5:
     print("erro digite numeros validos")



