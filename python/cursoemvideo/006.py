"""Reads number and prints double, triple and square root."""

number = float(input("Digite um número: "))
double_number = number * 2
triple_number = number * 3
sqrt_number = number ** (1 / 2)

print(
    f"O seu número é {number}, o dobro é {double_number}, o triplo é {triple_number}, e a raíz quadrada é {sqrt_number}"
)
