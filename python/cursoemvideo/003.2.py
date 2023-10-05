"""
Checks if user input is a number, sums and prints
"""


def input_number(number):
    """
    This function checks if user input is a number.
    :param user_input: float number
    """
    while True:
        try:
            user_input = float(input(number))
        except ValueError:
            print("Digite somente números, por favor.")
            continue
        else:
            return user_input


number1 = input_number("Digite um número: ")
number2 = input_number("Digite outro número: ")

sum_numbers = number1 + number2

print(f"A soma dos números {number1} e {number2} é {sum_numbers}")
