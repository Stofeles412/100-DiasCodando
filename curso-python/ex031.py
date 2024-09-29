distancia = float(input("qual é  a distancia da sua viajem km ?"))
valor = distancia * 0.50
desconto = distancia * 0.45
if distancia <= 200: print("de acordo com a distancia da sua viajem o valor será de R${:.2f}".format(valor))
else: print("o valor da viajem fica por R${:.2f}".format(desconto))
