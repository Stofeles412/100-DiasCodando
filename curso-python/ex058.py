from random import randint
pc = randint(0, 10)
print("Sou seu pc... Acabei de pensar em um numero entre 0 e 10: ")
print("Sera que  você comsegue imaginar qual foi ?")
acertou = False
palpites = 0
while not acertou:
      jogador = int(input("Qual é seu palpite ?"))
      if jogador > 10:
          print("Invalida, tente de 1 a 10")
      palpites += 1
      if jogador == pc:
          acertou = True
          
      if jogador < pc:
             print("Mais... tente novamente")
      else:
            print("Menos... tente novamente")
print("você acertou ! depois de {} tentativas".format(palpites))
