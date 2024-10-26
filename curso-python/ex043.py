peso = float(input("Qual é seu peso (kg)? "))
altura = float(input("Qual é sua altura (m)? "))
imc = peso / (altura ** 2)
print("Seu IMC é de {:.1f}".format(imc))

if imc < 18.5:
    print("Magreza Severa!")
elif 18.5 <= imc < 25:
    print("Peso normal!")
elif 25 <= imc < 30:
    print("Excesso de peso")
else:
    print("Obesidade")
