"""Prints arithmetic progression."""
first = int(input("Primeiro termo: "))
constant = int(input("Razão da PA: "))
term = first
counter = 1
total = 0
more = 10
while more != 0:
    total = total + more
    while counter <= total:
        print("{} → ".format(term), end="")
        term += constant
        counter += 1
    print("PAUSA")
    more = int(input("Quantos termos você quer mostrar a mais: "))
print(f"Progressão finalizada com {total} termos mostrados.")
