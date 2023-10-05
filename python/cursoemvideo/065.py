"""Reads numbers and prints max and min values."""
average = count = max = min = sum = 0
choice = "s"

while choice in "Ss":
    n = int(input("Digite um número: "))
    sum += n
    count += 1
    if count == 1:
        max = min = n
    else:
        if n > max:
            max = n
        if n < min:
            min = n
    choice = str(input("Quer continuar? [S/N] ").strip()[0])
average = sum / count
print("Acabou")
print(f"Você digitou {count} números e a média foi {average:.1f}")
print(f"O maior valor foi {max}, e o menor foi {min}")
