import moeda

p = float(input("Digte o preço: R$"))
print(f"A metade fica por R${p} {moeda.metade(p)}")
print(f"O doblo do valor de R${p} é {moeda.dobro(p)}" )
print(f"O valor de R${p} com 50% desconto fica por {moeda.menos(p,50)}")
print(f"O valor de R${p} 10% a mais fica por {moeda.aumentar(p,10)}")