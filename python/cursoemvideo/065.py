# Reads numbers and prints max and min values
average = count = max = min = sum = 0
choice = 's'

while choice in 'Ss':
	n = int(input('Digite um número: '))
	sum += n
	count += 1
	if count == 1:
		max = min = n
	else:
		if n > max:
			max = n
		if n < min:
			min = n
	choice = str(input('Quer continuar? [S/N] ').strip()[0])
average = sum / count
print('Acabou')
print('Você digitou {} números e a média foi {:.1f}'.format(count, average))
print('O maior valor foi {}, e o menor foi {}'.format(max, min))
