ficha = []
while True:
    nome = str (input("Nome:")).strip()
    nota1 = float (input("Nota 1:"))
    nota2 = float (input("Nota 2:"))
    media = (nota1 + nota2) / 2
    ficha.append( [nome, nota1, nota2, media])
    res = str(input("Deseja continuar [S/N]: ?")).strip().upper()
    if res in "N":
        break
print(f'"{"":4<}{"Nome":<10}{"Media":8>}')
for i, a in enumerate(ficha):
    print(f'{i:4<} {a[0]:<10}{a[2]:>8.1f}')
while True:
    print("=-"* 30)
    opc = int(input("Mostrar nota de  qual aluno: ? (999 interromper): "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print("<<<<<VOLTE SEMPRE >>>>")
        
    


