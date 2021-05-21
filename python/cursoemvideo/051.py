# Prints arithmetic progression of 10 numbers
print('10 Termos de uma PA')
number = int(input('Primeiro termo: '))
constant = int(input('Razão: '))
total = 0
for c in range (1, 11):
    total = number + (c - 1) * constant
    print('{}'.format(total), end = ' → ')
print('ACABOU')