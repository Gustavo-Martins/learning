"""Randon numbers printing."""
from random import randint

numbers = (
    randint(0, 99),
    randint(0, 99),
    randint(0, 99),
    randint(0, 99),
    randint(0, 99),
)

print(f"Os valores sorteados foram: {numbers}")
print(f"Maior valor: {max(numbers)}")
print(f"Menor valor: {min(numbers)}")
