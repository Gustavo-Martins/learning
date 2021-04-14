# Guessing game
from random import randint
from time import sleep


print(('-==') * 21)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(('-==') * 21)

number = int(input('Em qual número eu pensei? '))
rand = randint(0, 5)

print('PROCESSANDO...')
sleep(2)

if number == rand:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(rand, number))
