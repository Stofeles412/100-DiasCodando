from datetime import date
atual = date.today().year
totdemaior = 0
totdemenor = 0
for pessoas in range(1,8):
    nasc = int(input("Em que ano a {}° pessoa nasceu ?".format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        print("Essa pessoa é maior")
        totdemaior += 1
    else:
        print("essa pessoa é menor de idade")
        totdemenor += 1
print("Ao todo tivemos {} pessoas maior".format(totdemaior))
print("E {} pessoas menor de idade".format(totdemenor))
