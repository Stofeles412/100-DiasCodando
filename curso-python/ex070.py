total = maisMil = cont = 0
menor = float('inf') 
barato = ""

while True:
    produto = str(input("Nome do produto: ")).strip().upper()
    preço = float(input("Preço: R$")) 
    
    total += preço
    cont += 1  
    
    if preço > 1000:
        maisMil += 1
    
   
    if preço < menor:
        menor = preço
        barato = produto
    
    res = " "
    while res not in "SN":
        res = str(input("Quer continuar comprando? [S/N] ")).strip().upper()[0]
    
    if res == "N":
        break

print(f"\nO total de compras foi R${total:.2f}")
print(f"Você comprou {maisMil} produtos que custaram mais de R$1000.")
print(f"O produto mais barato foi {barato}, que custou R${menor:.2f}")
print("Obrigado por comprar conosco! Volte sempre :)")
