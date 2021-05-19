# Sum of multiple of 3 from 1 to 500
mult_sum = 0
total_numbers = 0
for c in range (1, 501, 1):
    if c % 2 != 0 and c % 3 == 0:
        total_numbers += 1
        mult_sum += c
print('A soma dos {} números múltiplos de 3 é: {}.'.format(total_numbers, mult_sum))
