res ="S"
soma = cont = media = maior = menor = 0
while res in "Ss":
    n = int(input("Digite um número"))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input("Quer continuar ? [S/N] ?")).upper().strip()
media = soma / cont
print("vc digitou {} números e a média = {}".format(cont, media))
print("E o maior valor foi {} e o menor foi {}".format(maior, menor))