while True:
	print('-' * 33)
	n = int(input('Quer ver a tabuada de qual valor? '))
	print('-' * 33)
	if n <= 0:
		print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
		break
	for c in range (1, 10):
		print(f'{n} X {c} = {n * c}')
