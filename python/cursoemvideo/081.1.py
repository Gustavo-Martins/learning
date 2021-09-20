# Prints reversed list
numbers = []
while True:
	n = int(input('Digite um valor: '))
	numbers.append(n)
	choice = str(input('Deseja continuar? [S/N] ').strip().lower()[0])
	if choice in 'n':
		break
print('-=' * 30)
print(f'Você digitou {len(numbers)} valores.')
numbers.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numbers}')
if 5 in numbers:
	print('O valor 5 faz parte da lista.')
else:
	print('O valor 5 não foi encontrado na lista')
