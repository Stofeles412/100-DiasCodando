tot18 = maisM = mulherMenos20 = 0
while True:
  
    idade = int(input("Idade: "))
    
   
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo [M/F]: ").strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == "M":
            maisM += 1
        if sexo == "F":
          if idade < 20:
            mulherMenos20 += 1
        
    
  
    res = " "
    while res not in "SN":
        res = input("Deseja continuar? [S/N]: ").strip().upper()[0]
    
  
    if res == "N":
        break

print(f"Total de epessoas com mais de 18 anos: {tot18} ")
print(f"Foi cadastrado um total de {maisM} pessoas do sexo masculino")
print(f"E foram cadastradas {mulherMenos20} mulheres com menos de 20 anos")

