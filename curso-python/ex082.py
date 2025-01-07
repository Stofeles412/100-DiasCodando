num = []
pares = []
impares = []
while True:
    num.append(int(input("Digite um numero:")))
    res = str(input("Deseja continuar? [S/N]")).upper().strip()
    if res in "N":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("-="* 30)
print(f"A lista completa é {num}")
print(f"Com os numeros impares a lista fica {impares}")
print(f"E com os numeros pares ficam {pares}")
        


    
    



