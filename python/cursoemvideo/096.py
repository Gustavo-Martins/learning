# Rectangular area calculation
def area(width, depth):
	return width * depth


print('Controle de Terrenos')
print('-' * 30)
width = float(input('LARGURA (m): '))
depth = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno de {width} x {depth} é de {area(width, depth)}m².')
