# Prints arithmetic progression
print('Gerador de PA')
print('-=-' * 10)
first = int(input('Primeiro termo:  '))
constant = int(input('Razão da PA: '))
number = first
counter = 1
terms = 10
additionalTerms = 1
total_terms = 0

while additionalTerms != 0:
	while counter <= terms:
		print('{}'.format(number), end = ' → ')
		number += constant
		counter += 1
	print('PAUSA')
	total_terms += terms
	additionalTerms = int(input('Quantos termos você quer mostrar a mais? '))
	counter = 1
	terms = additionalTerms
print('A progressão aritmética terminou com {} termos.'.format(total_terms))
