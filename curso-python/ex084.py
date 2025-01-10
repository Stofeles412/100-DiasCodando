galera = []
dados = list()
totalmai = totalmeno = 0
for c in range(0,3):
    dados.append(str(input("Nome")))
    dados.append(int(input("Idade: ")))
    galera.append(dados)
    dados.clear()
    for pessoa in galera:
     if dados[0] >= 18:
      totalmai += 1
     else:
       totalmeno += 1
print(f"Usuarios cadastrados {galera}")
print(f"E foram cadatradas {totalmai} maior de idade")
print(f"E {totalmeno} menor de idade")