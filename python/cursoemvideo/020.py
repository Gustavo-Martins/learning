# Reads list and prints in random order
from random import sample


name1 = str(input('Digite o primeiro nome: '))
name2 = str(input('Digite o segundo nome: '))
name3 = str(input('Digite o terceiro nome: '))
name4 = str(input('Digite o quarto nome: '))

name_list = [name1, name2, name3, name4]
chosen_order = sample(name_list, k=4)

print('A ordem de sorteio é: ')
print(chosen_order)
