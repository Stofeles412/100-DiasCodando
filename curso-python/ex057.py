sexo = str(input("digite seu sexo [M/F] ")).strip().upper()[0]
while sexo not in  "MF":
      sexo = str(input("Sexo inválido ! Tente novamente com F ou M")).strip().upper()[0]
print("Sexo {} cadastrado com sucesso !".format(sexo))