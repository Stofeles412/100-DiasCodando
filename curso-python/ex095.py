time = list()
dados = dict()
partidas = list()
while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    dados["gols"] = int(input("Quatos gols: "))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou: ?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int (input(f"Quantos gols na partida {c}° ?" )))
    dados["gols"] = partidas[:]
    dados["total"] = sum(partidas)
    time.append(dados.copy())
    while True:
        res = str(input("Deseja continuar ? [S/N] ")).upper()[0]
        if res in "SN":
         break
        print("ERRO !! Responda com apenas S - N ")
    
    if res == "N":
        break
print("_"* 30)
for k, v in enumerate(time):
    print(f"{k:>4}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-="*30)
        
    
    



