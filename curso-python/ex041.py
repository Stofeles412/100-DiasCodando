from datetime import date
nascimento = int(input("qual ano você nasceu ?"))
ano = date.today().year
idade = ano -  nascimento 
print("Com {} anos".format(idade))
if idade <= 9:
    print("Atleta Mirin")
elif idade <= 14:
    print("Atleta Infantil")
elif  idade <= 18:
    print("atleta Junior")
else:
    print("atleta Master")