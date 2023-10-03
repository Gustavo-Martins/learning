# Reads number and prints basic math operations
number = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    print("{} x {} = {}".format(number, c, (number * c)))
