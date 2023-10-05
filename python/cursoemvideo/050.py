"""Reads numbers and sums even numbers."""
counter = 0
total = 0
for c in range(1, 7):
    number = int(input(f"Digite o {c}º número: "))
    if number % 2 == 0:
        total += number
        counter += 1

print(f"A soma dos {counter} números pares digitados é: {total}")
