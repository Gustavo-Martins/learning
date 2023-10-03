# Prints list, evens list, and odds list
numbers = []
evens = []
odds = []

while True:
    n = int(input("Digite um valor: "))
    numbers.append(n)
    if n % 2 == 0:
        evens.append(n)
    elif n % 2 != 0:
        odds.append(n)
    choice = str(input("Deseja continuar? [S/N] ").strip().lower()[0])
    if choice in "n":
        break

print("=-" * 20)
print(f"Números digitados: {numbers}")
print(f"Números pares digitados: {evens}")
print(f"Números ímpares digitados: {odds}")
