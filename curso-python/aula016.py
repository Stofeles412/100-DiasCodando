num = [9, 2, 5, 4, 3, 0, 9, 3 ]
num[2] = 6
num.sort() #ordernar
num.append(10) #adicionar elemento na lista
num.pop(0) #para add removendo o ultimo elemento
num.remove(2) #remove um dos elmentos selecionando pelo indice
num.insert(1,1) #para inserir elementos na listas
if 5 in num:
    num.remove(8)
else:
    print('Nao achei o numero 4')
print(num)
print(f"essa LISTA TEM {len(num)} elemnetos")