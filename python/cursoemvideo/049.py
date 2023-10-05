"""Reads number and prints basic math operations."""
number = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    print(f"{number} x {c} = {number * c}")
