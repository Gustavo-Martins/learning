# Do basic math and print

number1 = float(input('Digite um valor: '))
number2 = float(input('Digite outro valor: '))


addition = (number1 + number2)
subtraction = (number1 - number2)
multiplication = (number1 * number2)
division = (number1 / number2)
floor_division = (number1 // number2)
modulus = (number1 % number2)
exponentiation = (number1 ** number2)

print('O valor da soma dos números é {}, e o da subtração é {}'.format(addition, subtraction))
print('O valor da divisão é {:.3f}, o da divisão inteira é {}, e o módulo é {}'.format(division, floor_division, modulus))
print('O valor da exponenciação é {}'.format(exponentiation))