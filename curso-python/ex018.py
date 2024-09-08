from math import radians, sin, cos, tan
angulo = float(input("digite o angulo"))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O Ângulo de {} tem o seno de {:.2f}".format(angulo,seno))
print ("O Ângulo de {} tem o cosseno de {:.2f}".format(angulo, cosseno))
print("O Ângulo de {} tem o targente de {:.2f}".format(angulo, tangente))