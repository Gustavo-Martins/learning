def flourish(size=35):
	"""Returns a string of '-'s."""
	return '-' * size


def menu_main():
	"""Prints main menu options."""
	print(flourish())
	print(f"{'MENU PRINCIPAL':^35}")
	print(flourish())
	print('1 - Ver pessoas cadastradas')
	print('2 - Cadastrar Novas Pessoas')
	print('3 - Sair do Sistema')
	print(flourish())


def menu_option(option):
	"""Prints selected main menu option."""
	print(f"Função menu_option recebeu: {option}")
	print(flourish())
	print(f"{'OPÇÃO' :^35}")
	print(flourish())
