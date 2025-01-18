dados = dict()
partidas = list()
dados["nome"] = str(input("Nome: "))
dados["gols"] = int(input("Quatos gols: "))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou: ?'))
for c in range(0, tot):
    partidas.append(int (input(f"Quantos gols na partida {c}° ?" )))
dados["gols"] = partidas[:]
dados["total"] = sum(partidas)
print("-="*30)
print(dados)
print("-="*30)
for k, v in dados.items():
    print (f"O campo {k} tem valor {v}") 
print("-="*30)
print(f"O jogador {dados['nome']} jogou {len (dados["gols"])} partidas")
for i, v in enumerate(dados["gols"]):
    print(f"=> Na partida {i} fez {v} gols")
    
print(f"Foi um total de gols {dados['total']} ")
