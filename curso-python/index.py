nome = input("Digite seu nome de usuário: ")

if nome.lower() == "fernando":
    print("Você não tem acesso.")
else:
    print("Seja bem-vindo(a) {}".format(nome))
