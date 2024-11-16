n1 = int(input("1° valor"))
n2 = int(input("2° valor"))
opçao  = 0
while opçao != 5:
 print("""
         [1] somar
         [2] multiplicar
         [3] maior
         [4] novos números
         [5] Sair do programa
     
         """)
opçao = str(input("Escolha a opção : "))
if opçao == 1:
   soma = n1 + n2
   print("A soma dos de {} + {} = {}".format(n1, n2, soma))