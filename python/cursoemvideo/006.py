# Reads number and prints double, triple and square root

number = float(input('Digite um número: '))
double_number = number * 2
triple_number = number * 3
sqrt_number = number ** (1/2)

print('O seu número é {}, o dobro é {}, o triplo é {}, e a raíz quadrada é {}'.format(number, double_number, triple_number, sqrt_number))
