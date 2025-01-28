

def voto (ano):
    from  datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade < 16 or idade > 65:
        return (f"Com a idade de {idade} anos não vota")
    elif idade <= 16 or idade > 65:
        return(f"Com {idade} anos Seu voto é opcional")
    else:
        return (f"Com {idade} anos você tem voto obrigartorio")
   
    
    
       
nascimento = int(input("Ano de nascimento: "))
print(voto(nascimento))