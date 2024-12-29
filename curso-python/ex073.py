times = ("Botafogo","Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São paulo", "Corithins", "Bahia", "Cruzeiro", "Vasco", "Vitória", "Atletico-MG", "Grêmio", "Juventude", "Bragantino", "Athetico-PR", "Criciúma", "Atlético-GO", "Cuiabá")
print(f"Lista de times do Brasileirão 2024: {times}")
for t in times:
    print(t)
print(f"Os 5 primeiros são {times[0:5]}")
print(f"Os 4 rebaixados são {times[15:20]}")
print(f"E o Campeão é o {times[0]} q terminou em 1 lugar ")
print(f"Os times em ordem alfabética: {sorted(times)}" )
print(f"E a chapecoense  ficou em 15 luagr da serie B")