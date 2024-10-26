num = int(input("digite um numero inteiro"))
print("""escolha uma das base de convesões
[1] convertar para binario
[2] converter para octal
[3] converter para hexadecimal""")
opção = int(input("escolha um dos numéros"))

if opção == 1:
    print("{} convertido para binario é igual {} ".format(num, bin(num)[2:]))
elif opção == 2:
    print("convertendo {} para octal fica {}".format(num, oct(num)[2:]))
elif opção == 3:
    print("convertendo o {} para hexadecimal fica {}".format(num, hex(num)[2:]))
else:
    print("erro por favor digite numeros válidos")