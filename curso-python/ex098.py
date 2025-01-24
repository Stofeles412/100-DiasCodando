from time import sleep
def contador(i, f, p):
    if p < 0:
        p*= -1
    if p == 0:
        p == 1
    print("-="*30)
    print(f"Contagem de {i} até o {f} passando de  {p}")
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
              print(f"{cont}", end="", flush=True)
              cont += p
              print(" Fim ")
        else:
            cont = i
            while cont >= f:
             print(f"{cont} ",end="", flush=True)
             sleep(0.5)
             cont -= p
        print(" Fim ")
    print("-="*30)
contador(1,10,1)
contador(10,0,2)
print ( "Agora é sua vez de personalizar!")
ini = int(input("inicio"))
fim = int(input("Fim"))
passo = int(input("Passos:"))
contador(ini, fim, passo)
