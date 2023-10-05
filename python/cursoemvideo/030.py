"""Reads number and prints if it is even or odd."""
number = int(input("Me diga um número inteiro qualquer: "))

if number % 2 == 0:
    print(f"O número {number} é PAR.")
else:
    print(f"O número {number} é ÍMPAR.")
