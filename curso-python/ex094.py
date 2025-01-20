dados = dict()
galera = list()
soma = 0

while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    
    while True:
        dados["sexo"] = str(input("Qual o sexo [F/M]: ")).strip().upper()[0]
        if dados["sexo"] in "MF":
            break
        print("ERRO! Tente novamente com M ou F.")
    
    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    galera.append(dados.copy())
    
    while True:
        res = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
        if res in "SN":
            break
        print("ERRO! Responda com S ou N.")
    
    if res == "N":
        break

print("-=" * 30)

# Cálculo e exibição de resultados
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos.")

# Mulheres cadastradas
print("C) As mulheres cadastradas foram: ", end="")
for p in galera:
    if p["sexo"] == "F":
        print(f"{p['nome']}", end=" ")
print()

# Pessoas com idade acima da média
print("D) Lista de pessoas com idade acima da média:")
for p in galera:
    if p["idade"] > media:
        print("   ", end="")
        for k, v in p.items():
            print(f"{k} = {v}; ", end="")
        print()

print(">>> ENCERRADO <<<")
