def leiaint(msg):
  while True:
    try:
      n = int(input(msg))
    except(ValueError, TypeError):
      print(' \033[31m Erro ! Por favor digite um valor válido\033[m')
      continue
    except(KeyboardInterrupt):
      print('\n\033[31m usuario não digitou valor\033[m')
      return 0
    else:
      return n
    
    
      
num = leiaint("Digite um valor:")
print(f'O valor digitado foi {num}')


def leiafloat(msg):
  while True:
    try:
      n = float(input(msg))
    except(ValueError, TypeError):
      print(' \033[31m Erro ! Por favor digite um valor válido\033[m')
      continue
    except(KeyboardInterrupt):
      print('\n\033[31m usuario não digitou valor\033[m')
      return 0
    else:
      return n
    
    
      
num = leiafloat("Digite um valor:")
n2 = leiafloat("Digite um valor float")
print(f'O valor digitado foi {num} e o float fou {n2}')