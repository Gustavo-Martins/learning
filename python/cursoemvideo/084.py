# Saves names and weights
people = []
data = []
min = max = 0

while True:
	data.append(str(input('Digite o nome: ')))
	data.append(float(input('Digite o peso: ')))
	if len(people) == 0:
		min = max = data[1]
	else:
		if data[1] > max:
			max = data[1]
		if data[1] < min:
			min = data[1]
	people.append(data[:])
	data.clear()
	choice = str(input('Deseja continuar? [S/N] ').strip().lower()[0])
	if choice in 'n':
		break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(people)} pessoas.')
print(f'O maior peso foi de {max} Kg. Peso de ', end='')
for p in people:
	if p[1] == max:
		print(f'{p[0]}', end=' ')
print('\n')
print(f'O menor peso foi de {min} Kg. Peso de ', end='')
for p in people:
	if p[1] == min:
		print(f'{p[0]}', end=' ')
