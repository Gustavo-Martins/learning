"""Reads float and prints price with discount."""

price = float(input("Digite o preço do produto: "))
discount = (price * 5) / 100
new_price = price - discount

print(
    f"O produto custa R$ {price:.2f}, com desconto de 5%, o produto custará: R$ {new_price:.2f}."
)
