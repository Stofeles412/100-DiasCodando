from time import sleep
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
    opçao = int(input("Escolha a opção : "))
    if opçao == 1:
       soma = n1 + n2
       print("A soma de {} + {} = {}".format(n1, n2, soma)) 
    elif opçao == 2:
        mult = n1 * n2
        print("A multiplicação de {} x {} = {}".format(n1, n2, mult))
    elif opçao == 3:
        if n1 > n2:
            print("O maior é {}".format(n1))
        else:
            print("O maior é o {}".format(n2))
    elif opçao == 4:
        n1 = int(input("1° valor"))
        n2 = int(input("2° valor"))
    else:

     sleep (2)

print("Finalizado com sucesso")


