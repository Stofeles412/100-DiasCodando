print("gerador de Pa")
print("-" * 30)
primeiro = int(input("Primeiro termo: "))
rz = int(input("Digite a razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} >".format(termo), end=" ")
    termo += rz
    cont += 1
    
