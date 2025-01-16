estado = dict()
brasil = list()
for c in range(0,3):
    estado ["sigla"] = str(input("Unidade federativa"))             
    estado["uf"] = str(input("Sigla do seue Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=" ")