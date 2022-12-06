from packages.interface.menu import menu_header, menu_option, menu_print_options


menu_header('MENU PRINCIPAL')
menu_options = ['Ver pessoas cadastradas', 
		'Cadastrar Novas Pessoas', 
		'Sair do Sistema']
menu_print_options(menu_options)


# menu_main()

while True:
	try:
		option = int(input('Digite uma opção: '))
		menu_option(option)

		if option < 1 or option > 3:
			print('Por favor, digite uma opção válida.')
		elif option == 3:
			print('Sistema encerrado. \nVolte sempre!')
			break
	except (TypeError, ValueError):
		print('Por favor, digite um número válido!')
