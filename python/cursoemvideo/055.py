# Reads 5 person weights and prints maximum and minimum values
minimum = 0
maximum = 0

for person in range(1, 6):
    weight = float(input("Digite o peso da {}ª pessoa: ".format(person)))
    if person == 1:
        minimum = person
        maximum = person
    else:
        if weight > maximum:
            maximum = weight
        if weight < minimum:
            minimum = weight

print(
    "O maior peso lido é {} Kg, e o menor peso lido é {} Kg.".format(maximum, minimum)
)
