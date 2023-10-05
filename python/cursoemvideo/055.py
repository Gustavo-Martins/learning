"""Reads 5 person weights and prints maximum and minimum values."""
minimum = 0
maximum = 0

for person in range(1, 6):
    weight = float(input(f"Digite o peso da {person}ª pessoa: "))
    if person == 1:
        minimum = person
        maximum = person
    else:
        if weight > maximum:
            maximum = weight
        if weight < minimum:
            minimum = weight

print(f"O maior peso lido é {maximum} Kg, e o menor peso lido é {minimum} Kg.")
