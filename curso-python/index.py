n1 = float (input("digite uma nota"))
n2 = float (input("digite outro numero"))
m = (n1 + n2)/2
print("a sua media foi {:.1f}".format(m))
if m >= 6.0:
   print("sua media foi boa parabens")
else: 
    print("sua media foi ruim :( estude mais !")