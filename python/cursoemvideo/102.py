def fat(n, show=True):
	"""Returns factorial of a number.
	
	Keywords arguments:
	n -- Integer to calculate factorial
	show -- default == 0 (optional) Shows the calculation
	"""
	counter = n
	fat = 1
	while counter > 0:
		if show:
			print(f'{counter}', end='')
			print(' x ' if counter > 1 else ' = ', end='')
		fat *= counter
		counter -= 1
	print(fat)


n = int(input('Digite um número para mostrar o fatorial: '))
fat(n)
