from packages.interface.menu import menu_main, menu_option


menu_main()

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
