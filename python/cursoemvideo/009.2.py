"""Reads integer and prints basic math operations."""


def input_integer(number):
    """Checks if input is valid int."""
    while True:
        try:
            number = int(input(number))
        except:
            print("Por favor, digite um número inteiro.")
        else:
            return number


numero = input_integer("Digite um número inteiro para ver a sua tabuada: ")


def basic_math():
    """Multiplies int from 1 to 10."""
    i = 1
    input_integer(numero)
    print(f"Número recebido {numero}")
    for n in range(1, 11):
        print("Teste")
        print(f"{numero * i}")
        i += 1


basic_math()
