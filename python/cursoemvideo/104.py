def read_int(msg):
	"""Validates if input is an integer."""
	ok = False
	value = 0
	while True:
		n = str(input(msg))
		if n.isnumeric():
			value = int(n)
			ok = True
		else:
			print('\033[0;31mERRO! Por favor, digite um número inteiro.\033[m')
		if ok:
			break
	return value


number = read_int('Digite um número: ')
print(f'Você digitou o número: {number}')
