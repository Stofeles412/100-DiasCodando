nota1 = float(input("qual sua primeira nota  ?"))
nota2 = float (input("E sua segunda nota ?"))
media = (nota1 + nota2) / 2
print("Sua media = {}".format(media))
if media < 5:
    print("Com a media de {:.1f} você estar de reprovado".format(media))
elif media > 5 and media < 7:
    print("Com a media de {:.1f} você estar de recuperação !".format(media))
else:
    print("Vc foi aprovado com uma nota de {:.1f} parabéns".format(media))
