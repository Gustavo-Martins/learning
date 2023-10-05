"""Calculates triangle rectangle hypotenuse."""
from math import pow
from math import sqrt


side1 = float(input("Digite a medida do primeiro cateto: "))
side2 = float(input("Digite a medida do segundo cateto: "))

hypotenuse = sqrt(pow(side1, 2) + pow(side2, 2))

print(f"A hipotenusa é: {hypotenuse:.2f}.")
