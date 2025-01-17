from random import randint
from time import sleep
from operator import itemgetter
jogo = {"jogador-1": randint(1, 6),
        "Jogador-2": randint(1,6),
        "Jogador-3":randint(1, 6),
        "Jogador-4": randint(1,6)}
rank = list()
print("Valores sorteados: ")

for k, v in jogo.items():
    print(f"{k} tirou {v} no dados")
    sleep (1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True )
print(rank)
print("RANK DOS JOGADORES")
print("-="*30)
for i, v in enumerate(rank):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}")
    sleep(1)
    
