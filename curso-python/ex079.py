valores = [] 
while True:
   n = (int( input("digite um valor:" )))
   if n not in valores:
       valores.append(n)
       print("Valor add com sucesso")
       escolha = str(input("Quer continuar [S/N]")).upper().strip()
   else:
        print("Valor duplicado, não vou add")
   if escolha in "Nn":
       break
        
       
       
print(f"Os valores digitados fora {sorted (valores)}")