# Customized counting
from time import sleep


flourish = ('-=' * 40)
def count(strt, ed, inc):
	print(flourish)
	print(f'Contagem de {strt} até {ed} de {inc} em {inc}:')
	
	# Prevents infinite counting
	if inc <0:
		inc *= -1
	# Prevents no counting
	if inc == 0:
		inc = 1
	if strt < ed:
		c = strt
		while c <= ed:
			# Flush prevents buffering in some terminals
			# so the count isn't displayed all at once after sleeping
			print(f'{c} ', end='', flush=True)
			sleep(0.3)
			c += inc
		print('FIM!\n')
	else:
		c = strt
		while c >= ed:
			print(f'{c} ', end='', flush=True)
			sleep(0.3)
			c -= inc
		print('FIM!\n')
	
count(1, 10, 1)
count(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(int(input('Passo: ')))
count(i, f, p)
