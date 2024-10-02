sal = float (input("Qual o salario do funcionario R$ ?"))
if sal <= 1250:
    novo =  sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print("O seu salario de {:.2f} com um aumento, você vai passar a ganhar R${:.2f}".format( sal, novo)) 
