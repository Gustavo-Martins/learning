# Checks if 3 sides make a triangle
print('-=-' * 16)
print('O valor de 3 retas forma um triângulo?')
print('-=-' * 16)
a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Esses três lados formam um triângulo.')
else:
    print('Esses três lados não formam um triângulo.')
