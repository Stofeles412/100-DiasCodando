print("gerador de Pa")
print("-" * 30)
primeiro = int(input("Primeiro termo: "))
rz = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while cont <= 10:
    print("{} >".format(termo), end=" ")
    termo += rz
    cont += 1
while mais != 0:
    total = total + mais
    while cont <= total:
     print("Pausa")
     mais = int(input("Quantos termos a mais você deseja mostrar ?"))
print("Fim")
