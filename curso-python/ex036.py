valor = float(input("qual o valore do imovél desejado ?"))
sal = float (input("qual é seu salário mensal ?"))
ano = int(input("em até quantos anos você deseja pagar ?"))
presta = .030 * sal
if presta <= sal:
    print("vc nn pode comprar !")
elif sal > presta:
    print("vc pode adquirir-la")