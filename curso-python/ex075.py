numero = (int(input("Digite um numero: ")),int(input("Digite outro numero: ")),int(input("Digite mais um numero: ")),int(input("Digite o ultimo numero: ")))
print(f"Vc digitou os valores{numero}")
print(f"O valor 9 apareceu {numero.count(9)} vezes ")
if 3 in numero:
    print(f"O valor 3 aparceu na {numero.index(3)+1}ª posição ")
else:
    print("O valor 3 não foi encontado em nehuma posição")
print(f"Os valores pares digitados fora {n}", end=" ")
if n in numero:
    if n % 2 == 0:
        print(n, end=" ")
        