# Checks if user input is a number, sums and prints


def inputNumber(number):
    while True:
        try:
            user_input = float(input(number))
            pass
        except ValueError:
            print("Digite somente números, por favor.")
            continue
        else:
            return user_input
            break


number1 = inputNumber("Digite um número: ")
number2 = inputNumber("Digite outro número: ")

sum = number1 + number2

print("A soma dos números {} e {} é {}".format(number1, number2, sum))
