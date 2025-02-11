def aumentar(preço, taxa = 0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)
    
def menos(preço, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)
    
    
def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)
    
    
def metade(preço = 0, formato=False):   
    res = preço / 2 
    return res if formato is False else moeda(res)
    
def moeda(preço = 0, moeda = "R$", formato =False):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print("-"*30)
    print("Resumo do valor".center(30))
    print(f"Preço analisando {moeda(preço)}")
    print("-"*30)
    print(f"Dobro do preço \t{dobro(preço, True)}")
    print(f"Metade do preço {metade(preço, True)}")
    print(f"{taxaa}% de aumento \t{aumentar(preço, taxaa, True)}")
    print(f"{taxar}% reduçao: \t{menos(preço,taxar, True)}")
    print("-"*30)
    print(">>> Fim <<<")