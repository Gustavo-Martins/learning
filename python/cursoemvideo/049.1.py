"""Reads number and inputs basic math operation."""
number = int(input("Digite um número para ver a sua tabuada: "))


def basic_math():
    """'Multiplies number from 1 to 10."""
    for c in range(1, 11):
        print(f"{number} x {c} = {number * c}")


basic_math()
