cadastro = ():
while True:
    nome = input("Qual o nome que quer cadastrar? ").strip()
    
    if nome not in cadastro:
        cadastro.append(nome)
        print("Nome cadastrado com sucesso!")
    else:
        print("Nome já cadastrado.")
    
    while True:
        mais = input("Deseja continuar? [S/N]: ").strip().upper()
        if mais in ["S", "N"]:
            break
        print("Resposta inválida. Digite 'S' para continuar ou 'N' para sair.")
    
    if mais == "N":
        print("Fim")
        break

print(f"Os nomes {cadastro} foram cadastrados com sucesso.")

