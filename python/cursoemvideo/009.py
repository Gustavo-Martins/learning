"""Reads integer and prints basic math operations."""

numero = int(input("Digite um número inteiro para ver a sua tabuada: "))


def basic_math():
    """Multiplies int from 1 to 10."""
    i = 1
    for n in range(1, 11):
        print(f"{numero * i}")
        i += 1


basic_math()
