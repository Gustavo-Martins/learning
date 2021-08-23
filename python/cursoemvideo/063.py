# Prints Fibonacci sequence
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end='')
counter = 3
while counter <= n:
	t3 = t1 + t2
	print(' → {}'.format(t3), end='')
	t1 = t2
	t2 = t3
	counter += 1
print(' → FIM')
