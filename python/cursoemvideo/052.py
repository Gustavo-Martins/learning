"""Reads number and prints if it's a prime number."""
number = int(input("Digite um número: "))
divisibles = 0

for c in range(1, number + 1):
    if number % c == 0:
        print("\033[33m", end="")
        divisibles += 1
    else:
        print("\033[31m", end="")
    print("{}".format(c), end=" ")

print(f"\n\033[mO número {number} foi divisível {divisibles} vezes.")
if divisibles > 2:
    print(f"O número {number} não é primo.")
else:
    print(f"O número {number} é primo.")
