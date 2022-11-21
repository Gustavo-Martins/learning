def check(msg):
	""""Checks if user input is a valid price.
	"""
	valid = False
	while not valid:
		usr_input = str(input(msg)).replace(',', '.').strip()
		print(f'Verificando {usr_input}')
		if usr_input.isalpha() or usr_input == '':
			print(f'ERRO \"{usr_input}" é um preço inválido.')
		else:
			valid = True
			return float(usr_input)
