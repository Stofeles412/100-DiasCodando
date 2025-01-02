valores = []
mai = 0
men = 0
for c in  range(0, 5):
    valores.append(int(input(f"digite um valor para a posição {c} >")))
    if c == 0:
      mai = men = valores[c]
    else:
       if valores[c] > mai:
           mai = valores[c]
       if valores[c] < men:
            men = valores[c]
print("=-"*30)
print(f"Você digitou os valores {valores}")
print(f"O maior valor foi o {mai} nas posições ",end=" ")
for i, v in enumerate(valores):
    if valores[i] == mai:
        print(f"{i}...", end=" ")
print(f"E o menor valor foi {men} nas posições ", end=" ")
for  i, v in enumerate(valores):
    if v == men:
        print(f"{i}...")
print()



