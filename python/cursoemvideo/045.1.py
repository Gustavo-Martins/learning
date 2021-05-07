# Rock, Papper, Scissors game
from random import randint
from time import sleep


print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
options = ('Pedra', 'Papel', 'Tesoura')
player = int(input('Qual a sua jogada? '))
if player in range (0, 3):
    computer = randint(0, 2)
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(1)
    print('PO!')
    print('Você jogou {}, e eu joguei {}.'.format(options[player], options[computer]))
    if player == computer:
        print('Nós fizemos a mesma jogada.')
        print('Empate!')
    elif player == 0 and computer == 2:
        print('Você venceu!')
    elif player == 0 and computer == 1:
        print('Você perdeu!')
    elif player == 1 and computer == 0:
        print('Você venceu!')
    elif player == 1 and computer == 2:
        print('Você perdeu!')
    elif player == 2 and computer == 1:
        print('Você venceu!')
    elif player == 2 and computer == 0:
        print('Você perdeu!')
else:
    print('Por favor, digite 0, 1 ou 2.')
