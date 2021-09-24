# Sorts odds and even numbers
numbers = [[], []]

for c in range (1, 8):
	n = int(input(f'Digite o {c}º valor: '))
	if n % 2 == 0:
		numbers[0].append([n])
	if n % 2 == 1:
		numbers[1].append([n])
		
print('-=' * 30)
print(f'Valores digitados: {numbers}')
print(f'Números pares: {numbers[0]}')
print(f'Números ímpares: {numbers[1]}')
