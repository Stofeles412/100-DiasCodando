import moeda

p = float(input("Digte o preço: R$"))
print(f"A metade fica por R${moeda.moeda(p,True)} {moeda.metade(p, True)}")
print(f"O dobro do valor de R${p} é {moeda.dobro(p, True)}" )
print(f"O valor de R${p} com 50% desconto fica por {moeda.menos(p,50, True)}")
print(f"O valor de R${p} 10% a mais fica por {moeda.aumentar(p,10, True)}")
