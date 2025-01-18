from datetime import datetime
dados = dict()
dados["nome"] = str(input("nome: "))
nasc = int(input('Data de nascimenti: '))
dados["idade"] = datetime.now().year - nasc
dados["ctps"] = int(input("Carteira de trabalho (0 não tem)"))
if dados["ctps" ] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["salário"] = float(input("Salário: R$ "))
    dados["Aposentadoria"] = dados["Contratação"] + 35 - datetime.now().year
for k, v in dados.items():
     print(f'- {k} tem o valor {v}')