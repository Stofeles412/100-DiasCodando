n = cont = soma = 0
n = int(input("Digite um número [999] para parar: "))
while n != 999:
  cont += 1
  soma += n
  n = int(input("Digite um número [999] para parar: "))
print("Acabou")
print("vc digitou  {} números".format(cont))
print("E a soma de todos é {}".format(soma))
