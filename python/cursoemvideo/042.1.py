# Checks if three sides make a triangle, and classify it
print('-=-' * 16)
print('O valor de 3 retas forma um triângulo?')
print('=-' * 16)
a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Esses lados formam um triângulo', end='')
    if a == b == c:
        print(' equilátero.')
    elif a == b or a == c or b == c:
        print(' isósceles.')
    elif a != b and a != c and b != c:
        print(' escaleno.')
else:
    print('Esses lados não formam um triângulo.')
