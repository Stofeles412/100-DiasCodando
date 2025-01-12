numeros = [[], []]
valores = 0
for c in range(1, 8):
    valores = (int(input(f"Digite o {c}° valor")))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
        numeros[0].sort()
        numeros[1].sort()
print(f"Os valores pares digitados foram {numeros[0]}")
print(f"E os valores imopares foram {numeros[1]}")
       

        
        
