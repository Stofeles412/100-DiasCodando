palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEMPYTHON", "CURSO","GRATIS","ESTUDAR", )
for p in palavras:
    print(f"\nNa palavra {p} temos as vogais")
    for letra in p:
        if letra.lower() in "aeiou":
         print(letra, end=" ")   
    