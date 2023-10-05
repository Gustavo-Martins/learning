"""Calculates triangle rectangle hypotenuse."""
from math import hypot


side1 = float(input("Digite a medida do primeiro cateto: "))
side2 = float(input("Digite a medida do segundo cateto: "))

hypotenuse = hypot(side1, side2)

print(f"A hipotenusa é: {hypotenuse:.2f}.")
