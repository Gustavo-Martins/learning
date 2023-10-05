"""Factorial calculator with fancy printing."""

n = int(input("Digite um número para calcular seu fatorial: "))
counter = n
f = 1  # Prevents multiplication by zero

print("Calculando {}! = ".format(n), end="")
while counter > 0:
    print("{}".format(counter), end="")
    print(" x " if counter > 1 else " = ", end="")
    f *= counter
    counter -= 1
print(f"{f}")
