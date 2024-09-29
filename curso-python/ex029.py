radar = float (input("qual velocidade vc passou ?"))
multa = (radar - 80) * 7
if radar > 80:
    print("Multado vc exerdeu o limite de velecidade de 80km/h")
    print("A multa foi no valor de de R${:.2f}".format(multa))
print("Dirija sempre, com segurança")


    