somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1,5):
    nome = str(input("Qual o nome da {}° pessoa ?".format(p))).strip()
    idade = int(input("Qual a idade ? "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
    
mediaidade = somaidade / 4
print ("A media de idade do grupo é {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho ))
print("E tem {} mulher com menos de 20 anos".format(totmulher20))