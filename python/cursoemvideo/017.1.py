# Calculates triangle rectangle hypotenuse
side1 = float(input('Digite o valor do cateto oposto: '))
side2 = float(input('Digite o valor do cateto adjacente: '))

hypotenuse = (side1 ** 2 + side2 ** 2) ** (1/2)

print('O valor do cateto oposto é {:.2f}, do cateto adjacente é {:.2f}, e da hipotenusa é {:.2f}'.format(side1, side2, hypotenuse))
