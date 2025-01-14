from random import randint
lista = []
jogos = []
print('=-'* 30)
print("JOGUE NA MEGA SENA")
print('=-'* 30)
quant = int(input("Quantos jogos você deseja sortear: ?"))
tot = 0
while tot <= quant:
    cont = 0
    while True:
      numero = randint(1,60)
      if numero  not in lista:
         lista.append(numero)
         cont += 1
      if cont >= 6:
        break 
lista.sort()
jogos.append(lista[:])
lista.clear()
print(f"As jogadas ficaram da seguinte forma {jogos}")

