# Picks random student from list
from random import choice


name1 = str(input('Digite o primeiro nome: '))
name2 = str(input('Digite o segundo nome: '))
name3 = str(input('Digite o terceiro nome: '))
name4 = str(input('Digite o quarto nome: '))

name_list = [name1, name2, name3, name4]
chosen = choice(name_list)

print('O aluno sorteado foi: {}'.format(chosen))
