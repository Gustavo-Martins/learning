person = {}
registry = []
choice = ' '

while True:
	person['name'] = str(input('Nome: '))
	person['sex'] = str(input('Sexo: [M/F] ').strip().upper()[0])
	while person['sex'] not in 'MF':
		print('ERRO! Por favor, digite apenas M ou F.')
		person['sex'] = str(input('Sexo: [M/F] ').strip().upper()[0])
	person['age'] = int(input('Idade: '))
	choice = str(input('Quer continuar? [S/N] ').strip().upper()[0])
	while choice not in 'SN':
		print('ERRO! Responda apenas S ou N.')
		choice = str(input('Quer continuar? [S/N] ').strip().upper()[0])
	registry.append(person.copy())
	print(person)
	person.clear()
	if choice in 'S':
		person['name'] = str(input('Nome: '))
		person['sex'] = str(input('Sexo: [M/F] ').strip().upper()[0])
		while person['sex'] not in 'MF':
			print('ERRO! Por favor, digite apenas M ou F.')
			person['sex'] = str(input('Sexo: [M/F] ').strip().upper()[0])
		person['age'] = int(input('Idade: '))
		print(person)
		registry.append(person.copy())
		choice = str(input('Quer continuar? [S/N] ').strip().upper()[0])
		while choice not in 'SN':
			print('ERRO! Responda apenas S ou N.')
			choice = str(input('Quer continuar? [S/N] ').strip().upper()[0])
	if choice in 'N':
		break
print(registry)
