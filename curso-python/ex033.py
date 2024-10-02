a = int (input("digite o primeiro valor"))
b = int (input("digite o segundo valor"))
c = int (input("digite o terceiro valor"))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
        menor = c


maior = a
if b>a and b>c:
    maior = a
if c>a and c>b:
    maior = c 
print("O menor valor é o {}".format(menor))
print("o maior valor digitando foi p {}".format(maior))
  