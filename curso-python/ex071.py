print("="* 30)
print("{:^30}""".format("banco vida"))
print("="*30)
valor = int (input("Quanto vc deseja sacar ? R$ "))
total = valor
ced = 50
totalCed = 0
while True:
    if total >= ced:
        total -= ced
    else:
        print(f"Total de {totalCed}x celulas de {ced}R$")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if total == 0:
            break
             
        

