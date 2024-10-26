from datetime import date
nascimento = int(input("digite sua data de nascimento"))
ano = date.today().year
idade = ano - nascimento
if idade == 18:
    print ("você deve se alistar IMEDIATMNETE")
elif idade < 18:
    saldo = 18 - idade
    print("Que pena, Ainda não chegou sua hora de se alistar, falta {} anos para seu alistamento".format(saldo))

elif idade > 18:
    saldo = idade - 18
    print("vc devia já estar alistado {} anos atrás".format(saldo))
    
    
   