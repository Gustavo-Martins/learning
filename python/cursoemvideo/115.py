from packages.data.check import read_int
from packages.interface.menu import menu_header, menu_option, menu_print_options


menu_header('MENU PRINCIPAL')
menu_options = ['Ver pessoas cadastradas', 
		'Cadastrar Novas Pessoas', 
		'Sair do Sistema']
menu_print_options(menu_options)

while True:
	option = read_int('Digite uma opção: ')

	if option < 1 or option > 3:
		print('Por favor, digite uma opção válida.')
	elif option == 3:
		print('Sistema encerrado. \nVolte sempre!')
		break
	else:
			menu_option(option)
