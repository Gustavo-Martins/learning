from packages.data.check import read_int
from packages.files.writing import create_file, file_exists, read_file, write_to_file
from packages.interface.menu import menu_header, menu_option, menu_print_options


file = 'pessoas.txt'

if not file_exists(file):
	create_file('pessoas.txt')

menu_header('MENU PRINCIPAL')
menu_options = ['Ver pessoas cadastradas', 
		'Cadastrar Novas Pessoas', 
		'Sair do Sistema']
menu_print_options(menu_options)


while True:
	option = read_int('Digite uma opção: ')

	if option < 1 or option > 3:
		print('Por favor, digite uma opção válida.')
	elif option == 1:
		read_file(file)
	elif option == 2:
		menu_header("NOVO CADASTRO")
		name = str(input("Nome: "))
		age = read_int("Idade: ")
		write_to_file(file, name, age)
	elif option == 3:
		print('Sistema encerrado. \nVolte sempre!')
		break
	else:
			menu_option(option)
