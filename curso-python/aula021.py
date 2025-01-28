
#def somar(a=0,b=0,c=0):
   # s = a + b + c
    #return s
#r1 = somar(3,2,5)
#r2 = somar(1,7)
#r3 = somar(4, 45)
#print(f"A soma vale {r1} {r2} e {r3}")
    
    
#somar()#

#def teste():
   # a = 3 
    #b = 4
   # c = 2
   # print(f"A: dentro vale {a}")
   # #print(f"B: dentro vale {b}")
    #print(f"C: dentro vale {c}")
#a = 5
#teste()
#print(f"A fora vale {a}")
def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f
f1 = factorial (5)
f2 = factorial (4)
f3 = factorial()
n = int(input("Digite um numero: "))
print(f"O factorial de {n} é {f1} {f2} e {f3}")



