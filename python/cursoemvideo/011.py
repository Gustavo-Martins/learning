# Reads float and prints paint required to paint area of wall

width = float(input("Digite a largura da parede (m): "))
height = float(input("Digite a altura da parede (m): "))

area = width * height
paint = area / 2

print(
    "Sua parede tem a dimensão de {:.2f}x{:.2f} m e sua área é de {:.2f} m².".format(
        width, height, area
    )
)
print("Para pintar essa parede, você precisará de {:.2f} L de tinta.".format(paint))
