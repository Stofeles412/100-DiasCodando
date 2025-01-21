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
        partidas.append(int (input(f"Quantos gols na partida {c +1}° ?" )))
    dados["gols"] = partidas[:]
    dados["total"] = sum(partidas)
    time.append(dados.copy())
    while True:
        res = str(input("Deseja continuar ? [S/N] ")).upper()[0].strip()
        if res in "SN":
         break
        print("ERRO !! Responda com apenas S - N ")
    if res == "N":
        break
print("-="* 30)
print("cod ", end="")
for i in dados.keys():
    print(f"{i:<15}", end="")
print()   
print("_"* 30)
for k, v in enumerate(time):
    print(f"{k:>4}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-="*40)
while True:
    busca = int(input("Qual jogador deseja mostrar (999 para parar)" ))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! não existe jogador com o codigo {busca}")   
    else:
        print(f"levantamento do jogador {time[busca]['nome']}:")  
        for i, g in enumerate(time[busca]['gols']):
            print(f"  No jogo {i} fez {g} gols")
        print("_"* 30)   
print("<<< Volta sempre :) <<<")   
    
    



