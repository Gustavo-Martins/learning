# Reads 3 numbers and prints highest and lowest values
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))

# Sorts lowest number
lowest = number1
if number2 < number1 and number2 < number3:
    lowest = number2
if number3 < number1 and number3 < number2:
    lowest = number3
# Sorts highest number
highest = number1
if number2 > number1 and number2 > number3:
    highest = number2
if number3 > number1 and number3 > number2:
    highest = number3

print('O menor número é: {}'.format(lowest))    
print('O maior número é: {}'.format(highest))