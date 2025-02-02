from time import sleep

c = ("\033[0;30;41m",  # 1 vermelho
     "\033[0;30;42m",  # 2 verde
     "\033[0;30;43m",  # 3 amarelo
     "\033[0;30;44m",  # 4 azul
     "\033[0;30;45m",  # 5 roxo
     "\033[7;30m",     # 6 branco
     "\033[m")         # Resetar cor

def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'", 4)
    print(c[6], end="")  # Cor branca para melhor visualização
    help(com)
    print(c[6], end="")  # Resetando cor
    sleep(1)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")  # Removido erro `end=True`
    print("~" * tam)
    print(f"  {msg}  ")  # Centraliza melhor o texto
    print("~" * tam)
    print(c[6], end="")  # Resetando cor para evitar problemas

# Programa principal
comando = ""
while True:
    titulo("Sistema de ajuda pyHelp", 3)
    comando = str(input("Função ou biblioteca > ").strip())
    if comando.upper() == "fim":
       break
    else:
        ajuda(comando)

titulo("Até logo!", 1)
