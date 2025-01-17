from datetime import datetime
dados = dict()
dados ["Nome"] = str(input("Qual o nome do CLT: ?"))
nasc = int(input("Digite o ano de nascimento contribuiente: "))
dados["idade"] = datetime.now().year - nasc
dados["Ctps"] = int(input("Carteira de trabalho(0 não tem): "))
if dados["Ctps"] != 0:
    dados["Contartação"] = int(input("ano de contratção: "))
    dados["Salario"] = float(input("Qual o salrio do CLT: R$"))
    dados["aponsentadoria"] = dados["idade"] + ((dados["Contratação"] + 35) - datetime.now().year)
print("-="*30)
for k, v in dados.items():
    print(f"_ {k} tem o valor {v}")
   
