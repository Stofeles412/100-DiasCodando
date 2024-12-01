from random import randint

v = 0
while True:
    jogador = int(input("Diga um valor: "))
    pc = randint(0, 10)  # Inclui o 0 como opção válida
    total = jogador + pc
    tipo = " "
    while tipo not in "PI":
        tipo = input("Par ou Ímpar [P/I]? ").strip().upper()[0]
    print(f"Você jogou {jogador} e o PC {pc}. Total de {total}.")
    print("Deu PAR!" if total % 2 == 0 else "Deu ÍMPAR!")

    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu :) !!")
            v += 1
        else:
            print("Você perdeu :( !!")
            input("Pressione Enter para encerrar o jogo.")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceu :) !!")
            v += 1
        else:
            print("Você perdeu :( !!")
            input("Pressione Enter para encerrar o jogo.")
            break

    print("Vamos jogar novamente!")

print(f"Game Over! Você venceu {v} vezes.")
