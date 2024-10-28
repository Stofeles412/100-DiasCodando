from random import randint
from time import sleep
itens = ("Pedra", "papel", "tesoura")
computador = randint(0, 2)
jogador = int(input("Qual é sua jogada ?"))
print("pedra...")
sleep (1)

print("papel...")
sleep(1)
print("tesoura...")
sleep (1)
print("""
      Suas opções:
      [0] Pedra
      [1] papel
      [2] Tesoura
      """)
print("O Pc Jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
if computador == 0: # pc jogou 0 = pedra
   if jogador == 0:
       print("empate")
   elif jogador == 1:
       print("O jogador venceu")
   elif jogador == 2:
        print("O pc venceu")
   else:
       print("jogada inválida")
       
elif computador == 1: # o pc jogou papel = 1
    if jogador == 0: 
        print("O Pc venceu")
    elif jogador == 2 : 
        print("O Jogador venceu")
    else:
        print("jogada inválida")
    
elif computador == 2: # o pc jogou tesoura = 2
    if jogador == 0:
        print("o jogador venceu")
    elif jogador == 1:
        print("o Pc venceu")
    elif jogador == 2:
        print("empate")
    else:
        print("jogada inválida")
