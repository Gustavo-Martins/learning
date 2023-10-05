"""Calculates triangle rectangle hypotenuse."""
side1 = float(input("Digite o valor do cateto oposto: "))
side2 = float(input("Digite o valor do cateto adjacente: "))

hypotenuse = (side1**2 + side2**2) ** (1 / 2)

print(
    f"O valor do cateto oposto é {side1:.2f}, do cateto adjacente é {side2:.2f}, e da hipotenusa é {hypotenuse:.2f}"
)
