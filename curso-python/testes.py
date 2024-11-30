n = s = 0
while True:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    s += n
#print("A soma vale {}".format(s))
print(f"A soma vale {s}")
