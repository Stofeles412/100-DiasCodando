a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f"Lista A: {a} ")
print(f"b Lista B: {b} ")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
valores.append(10)
for  c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}")
