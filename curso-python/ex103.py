def jogador(show=False ):
    caro = str(input("Nome do jogador: "))
    gol = int(input(f"Quantos gols {caro} fez: ?"))
    if caro == "" or caro == int:
        return("Jogador desconhedido fez 0")
    else:
        return(f"jogador {caro} fez {gol} gols")