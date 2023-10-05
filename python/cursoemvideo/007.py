"""Reads two grades and prints arithmetic mean."""

grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))


mean = (grade1 + grade2) / 2

print("A média das notas é: {:.1f}".format(mean))
