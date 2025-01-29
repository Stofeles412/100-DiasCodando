def ficha(jog="<desconhecido>",gol=0):
    print(f"O jogador {jog} fez {gol} gol(s) no campeonato" )
    
n = input("Nome do jogador: ").strip()
g = input("Quantos gols fez: ?").strip()
if g.isnumeric():
   g = int(g)
else:
    g = 0
if n == "" or n.isnumeric():
    ficha(gol=g)
else: 
  ficha(n,g)
        