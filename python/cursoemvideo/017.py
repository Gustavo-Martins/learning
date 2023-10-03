# Calculates triangle rectangle hypotenuse
from math import pow
from math import sqrt


side1 = float(input("Digite a medida do primeiro cateto: "))
side2 = float(input("Digite a medida do segundo cateto: "))

hipotenuse = sqrt(pow(side1, 2) + pow(side2, 2))

print("A hipotenusa é: {:.2f}.".format(hipotenuse))
