dados = dict()
galera = list()
while True:
   
    dados = {}
    dados["nome"] = str(input("Nome: "))
    while True:
        dados["sexo"] = str(input("Qual o sexo [F/M]: ")).strip().upper()[0]
        if dados["sexo"] in "MF":
            break
        print("ERRO !! Tente novamente com M ou F:")
    dados["idade"] = int(input("Idade: "))
    galera.append(dados.copy())
    while True:
        res = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
        if res in "SN":
            break
        print("Erro! Responda com S ou N.")
    if res == "N":
        break
    print("-=" * 30)
print(dados)
