def linha(tam = 42):
    return '_' * tam

def cabeçalho(txt):
    print (linha())
    print(txt)
    print(linha())

def menu (lista):
    cabeçalho('Menu principal')
    print(lista)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    