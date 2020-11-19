# Reads list and prints in random order
from random import shuffle


name1 = str(input('Digite o primeiro nome: '))
name2 = str(input('Digite o segundo nome: '))
name3 = str(input('Digite o terceiro nome: '))
name4 = str(input('Digite o quarto nome: '))

name_list = [name1, name2, name3, name4]
shuffle(name_list)

print('A ordem sorteada é: ')
print(name_list)
