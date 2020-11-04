# Reads number, remove decimals and print
from math import trunc


number = float(input('Digite um número: '))
whole_number = trunc(number)
print('A parte inteira de {} número é {} '.format(number, whole_number))
