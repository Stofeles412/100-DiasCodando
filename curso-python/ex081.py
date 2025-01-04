lista = list()
while True:
    lista.append(int(input("Digite um valor: ")))
    res = str(input("Deseja continuar [S/N] ?" )).upper().strip()
    if res == "N":
        break
print(f"O valores digitados foram {lista}")
print(f"Foram digitados {len(lista)} valores")
lista.sort(reverse=True)
print(f"Os valores em ordem decresente são {lista}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista em {cont} ocasioes")
else:
    print("Não o valor 5 não estar. Mas  pode ser adicionado na lista.")
