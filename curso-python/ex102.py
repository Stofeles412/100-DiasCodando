"""> calcular factorial de um numero
: param n: o numero a ser calculado
param show: (opcional) mostar ou não a conta
: return: o valor dp fatorial de um numero n"""
def factorial(n, show =False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c , end="")
            if c > 1:
                print("  x  ", end="")
            else:
             print(" = " , end="")
        f *= c
    return f
print(factorial(5 , show=True))
help(factorial)