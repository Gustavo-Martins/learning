# Reads number and prints if it's a prime 'number
number = int(input("Digite um número: "))
divisibles = 0

for c in range(1, number + 1):
    if number % c == 0:
        print("\033[33m", end="")
        divisibles += 1
    else:
        print("\033[31m", end="")
    print("{}".format(c), end=" ")

print("\n\033[mO número {} foi divisível {} vezes.".format(number, divisibles))
if divisibles > 2:
    print("O número {} não é primo.".format(number))
else:
    print("O número {} é primo.".format(number))
