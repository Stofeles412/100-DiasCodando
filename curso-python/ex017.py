from math import hypot
co = float (input("comprimento do cateto oposto"))
ca = float (input("o conmprimento do cateto adjacente"))
hi = hypot(co, ca)
"""hi = float ( co ** 2 + ca ** 2) ** (1/2)"""
print("a hipotenusa vai medir  {:.2f} " .format(hypot(hi)))