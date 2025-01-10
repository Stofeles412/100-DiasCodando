princ = list()
maior = menor = 0

while True:
    temp = list()
    temp.append(str(input("Digite o nome: ")))
    temp.append(float(input("Digite o peso da pessoa cadastrada (kg): ")))
    
    if len(princ) == 0:  
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    
    princ.append(temp[:]) 
    
    res = input("Deseja continuar [S/N]? ").strip().upper()
    if res == "N":
        break

print("=-" * 30)
print(f"As pessoas cadastradas foram: {princ}")
print(f"Ao todo foram cadastradas {len(princ)} pessoas.")
print(f"O mais pesado foi {maior}kg. Peso de ", end="")
for pessoa in princ:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}] ", end="")
print()
print(f"O mais leve foi {menor}kg. Peso de ", end="")
for pessoa in princ:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}] ", end="")
print()
