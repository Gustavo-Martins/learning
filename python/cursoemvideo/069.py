# Age and gender classification
adults = men = young_woman = 0
flourish = ('-' * 25)

while True:
	print(flourish)
	print('CADASTRE UMA PESSOA')
	print(flourish)
	age = int(input('Idade: '))
	if age >= 18:
		adults += 1
	gender = ' '
	while gender not in 'mf':
		gender = str(input('Sexo: [M/F] ').lower().strip()[0])
	if gender == 'm':
		men += 1
	elif gender == 'f' and age < 20:
		young_woman += 1
	choice = ' '
	while choice not in 'sn':
		choice = str(input('Quer continuar? [S/N] ').lower().strip()[0])
	if choice == 'n':
		break
print(f'Total de pessoas com mais de 18 anos: {adults}')
print(f'Temos homens {men} cadastrados.')
print(f'E temos {young_woman} mulheres com menos de 20 anos.')
