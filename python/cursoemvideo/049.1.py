# Reads number and inputs basic math operation
number = int(input("Digite um número para ver a sua tabuada: "))


def basicMath():
    for c in range(1, 11):
        print("{} x {} = {}".format(number, c, (number * c)))


basicMath()
