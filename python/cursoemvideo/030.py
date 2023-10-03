# Reads number and prints if it is even or odd
number = int(input("Me diga um número inteiro qualquer: "))

if number % 2 == 0:
    print("O número {} é PAR.".format(number))
else:
    print("O número {} é ÍMPAR.".format(number))
