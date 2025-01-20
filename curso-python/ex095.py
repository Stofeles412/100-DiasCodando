dados = dict()
registros = list()
while True:
    dados["nome"] = str(input("Digite seu nome: ? "))
    dados["idade"] = int(input("Digite sua idade: "))
    dados["Estado"] = str(input("Qual estado você reside: ?"))
    res = str(input("Deseja continuar: ? [S/N]")).upper().strip()
    if res == "N":
        break
print(dados)