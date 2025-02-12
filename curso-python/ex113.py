def leiaint(msg):
  while True:
    try:
      n = int(input(msg))
    except(ValueError, TypeError):
      print(' \033[31m Erro ! Por favor digite um valor válido\033[m')
      continue
    else:
      return n
    
    
      
num = leiaint("Digite um valor:")
print(f'O valor digitado foi {num}')