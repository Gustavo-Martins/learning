"""Reads float and prints price with discount."""

price = float(input("Digite o preço do produto: R$ "))
new_price = price - (price * 5 / 100)

print(
    f"O preço do produto é R$ {price:.2f}, com desconto de 5%, custará R$ {new_price}."
)
