"""Reads float and prints paint required to paint area of wall."""

width = float(input("Digite a largura da parede (m): "))
height = float(input("Digite a altura da parede (m): "))

area = width * height
paint = area / 2

print(
    f"Sua parede tem a dimensão de {width:.2f}x{height:.2f} m e sua área é de {area:.2f} m²."
)
print(f"Para pintar essa parede, você precisará de {paint:.2f} L de tinta.")
