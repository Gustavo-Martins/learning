# Odds and Evens game
from random import randint


wins = 0
flourish = ('=-=' * 15)
print(flourish)
print('VAMOS JOGAR PAR OU ÍMPAR')
print(flourish)
while True:
	player = int(input('Diga um valor: '))
	choice = ' '
	while choice not in 'pií':
		choice = str(input('Par ou Ímpar? [P/I]: ')).lower().strip()[0]
	computer = randint(0, 11)
	sum = player + computer
	print('-' * 45)
	print(f'Você jogou {player} e o computador {computer}. A soma é {sum}.')
	print('-' * 45)
	if sum % 2 == 0 and choice in 'p' or sum % 2 != 0 and choice in 'ií':
		print('Você VENCEU!')
		print('Vamos jogar novamente...')
		print(flourish)
		wins += 1
	else:		
		print('Você PERDEU!')
		break
print(flourish)
print(f'GAME OVER! Você venceu {wins} vezes.')
