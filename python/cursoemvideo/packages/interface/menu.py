def flourish(size=35):
	"""Prints a string of '-'s."""
	print('-' * size)


def menu_main():
	"""Prints main menu options."""
	flourish()
	print(f"{'MENU PRINCIPAL':^35}")
	flourish()
	print('1 - Ver pessoas cadastradas')
	print('2 - Cadastrar Novas Pessoas')
	print('3 - Sair do Sistema')
	flourish()


def menu_option(option):
	"""Prints selected main menu option."""
	print(f"Função menu_option recebeu: {option}")
	flourish()
	print(f"{'OPÇÃO' :^35}")
	flourish()
