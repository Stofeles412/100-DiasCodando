valor = float(input("qual o valore do imovél desejado R$ ?"))
sal = float (input("qual é seu salário mensal R$ ?"))
anos = int(input("em até quantos anos você deseja pagar ?"))
presta = valor / (anos * 12)
minimo = sal * 30 / 100
print("para pagar uma casa de {:.2f} em {} anos".format(valor, anos))
print("A prestação será de {:.2f}R$ ".format(presta))
if presta <= minimo:
    print("o emprestimo pode ser concedido")
else:
    print("o emprestimo foi NEGADO !")