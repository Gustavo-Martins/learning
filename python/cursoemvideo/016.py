"""Reads number, remove decimals and print."""
from math import trunc


number = float(input("Digite um número: "))
whole_number = trunc(number)
print(f"A parte inteira de {number} número é {whole_number} ")
