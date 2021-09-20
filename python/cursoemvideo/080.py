# Stores values in ordered list
flourish = ('=-' * 30)
numbers = []
for c in range (0,5):
	n = int(input('Digite um valor: '))
	if c == 0 or n > numbers[-1]:
		numbers.append(n)
		print('Adicionado no final da lista...')
	else:
		pos = 0
		while pos < len(numbers):
			if n <= numbers[pos]:
				numbers.insert(pos, n)
				print(f'Valor adicionado na posição {pos} da lista...')
				break
			pos += 1
		
print(flourish)
print(f'Os valores digitados em ordem foram: {numbers}')
