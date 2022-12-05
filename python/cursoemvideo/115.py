flourish = ('-' * 35)

print(flourish)
print(f"{'MENU PRINCIPAL':^35}")
print(flourish)
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar Novas Pessoas')
print('3 - Sair do Sistema')
print(flourish)

while True:
	try:
		option = int(input('Digite uma opção: '))
		print(option)
		if option < 1 or option > 3:
			print('Por favor, digite uma opção válida.')
		elif option == 3:
			print('Volte sempre!')
			break
	except (TypeError, ValueError):
		print('Por favor, digite um número válido!')
