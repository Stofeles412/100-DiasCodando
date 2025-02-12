try:
    def leiaint(msg):
    ok = False
    while True:
      n = str(input(msg))
      if n.isnumeric():
            valor = int(n)
            ok = True
      else:
             print("\033[0;31m erro! prfv digite valores validos. \033[m")
      if ok:
              break
    return valor

n = leiaint("Digite um numero: ")
print(f"Vc acabou de digitar o numero {n}")

    