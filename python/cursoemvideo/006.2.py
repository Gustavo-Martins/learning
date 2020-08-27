# Reads a number and prints double, triple and square root

number = float(input('Digite um número: '))

print('O seu número é {}. \nO dobro é {}. \nO triplo é {}. \nA raíz quadrada é {:.2f}.'.format(number, (number*2), (number*3), (number**(1/2))))


