from random import choice
aluno1 = input("primeiro aluno:")
aluno2 = input("segundo aluno:")
aluno3 = input("terceiro aluno:")
aluno4 = input("quarto aluno")
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print("O aluno sorteado foi {}".format(escolhido))


