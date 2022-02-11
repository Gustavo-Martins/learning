from random import randint


bets = list()
numbers = list()
sequences = 1
flourish = ('=-' * 30)

print(flourish)
print(' ' * 10, 'GERADOR DE APOSTAS', ' ' * 10)
print(flourish)
n_bets = int(input('Quantos jogos você quer que eu sorteie? '))

while sequences <= n_bets:
	c = 0
	while True:
		n = randint(1, 60)
		if n not in numbers:
			numbers.append(n)
			c += 1
		if c >= 6:
			break
	numbers.sort()
	bets.append(numbers[:])
	numbers.clear()
	sequences += 1

print('-=' * 3, f'JOGOS SORTEADOS', '=-' * 3)
for i, l in enumerate(bets):
	print(f'Jogo {i+1}: {l}')
print('-=' * 3, f'BOA SORTE!', '=-' * 3)
