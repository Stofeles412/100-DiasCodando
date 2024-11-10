num = int(input("digite um número: "))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print("\033[32m ", end= " ")
        tot += 1
    else:
        print("\033[31m ", end= " ")
    print("{}".format(c), end= " ")
print("\n\033[m0 O numero {} foi divísivel {} vez".format(num, tot))
if tot == 2:
    print("\033[32m Por isso ele é primo ! ")
else:
    print("\033[031m Por isso ele não é primo !")
    
