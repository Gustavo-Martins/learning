# Reads numbers and sums even numbers
counter = 0
total = 0
for c in range (1, 7):
    number = int(input('Digite o {}º número: '.format(c)))
    if number % 2 == 0:
        total += number
        counter += 1

print('A soma dos {} números pares digitados é: {}'.format(counter, total))
