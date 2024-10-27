print("{:=^80}".format(" Lojas guanabra"  ))
preço = float(input("preço das compras"))
print("""Formas de pagamneto
[1] à vista em dinheiro ou pix
[2] A vista no cartão
[3] 2x no cartão de crédito
[4] 3x ou mais
      
      """)
opçao = int(input("Qual é a opção "))
if opçao == 1:
    total = preço - (preço * 10 / 100)
    
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
      total = preço
      parcela = total / 2
      print("Sua compra será parcelada em 2x de {:.2f}R$ sem juros".format( parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas você deseja ?"))
    parcela = total / totparc
    print("Sua compra será parcela em {}x vezes de {:.2f}R$ com juros".format( totparc, parcela))
else:
    total = preço
    print("Opção inválida de pagamneto")
print("E sua compra de {:.2f} ficará por {:.2f}R$".format(preço, total))

 
