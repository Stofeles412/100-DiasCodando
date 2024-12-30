listagem = ("Lapis", 1.75, 
            "Borracha", 2.00
            ,"Caderno",15.90
            ,"estojo", 25.00
            ,"Tranferidor", 4.20
            ,"compasso", 9.99
            , "Moachila", 120.32
            ,"Canetas", 22.30
            , "Livro", 34.90)
print("-"*30)
print("Liatgem de preços")
print("-"*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
     print(f"{listagem[pos]:.<30}", end=" ")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-"*40)
    