print("-="*20)
print("analisador de triângulos")
print("-=" *20)
r1 = float (input("digite o primeiro seguimento"))
r2 = float (input("digite o segundo seguimento"))
r3 = float (input("digite o terceiro seguimento"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos a cima, formam um triângulo, ",  end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Os seguimentos não formam um trianâgulo")