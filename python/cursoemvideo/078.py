# Prints max and min values in a list and their positions
values = []
flourish = "=-" * 30
max = 0
min = 0

for c in range(0, 5):
    values.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        max = min = values[c]
    else:
        if values[c] > max:
            max = values[c]
        if values[c] < max:
            min = values[c]

print(flourish)
print(f"Você digitou os valores: {values}")
print(f"O maior valor foi {max}, nas posições ", end="")
for i, v in enumerate(values):
    if v == max:
        print(f"{i}...", end="")

print(f"\nO menor valor foi {min}, mas posições ", end="")
for i, v in enumerate(values):
    if v == min:
        print(f"{min}...", end="")
