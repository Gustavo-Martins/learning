# Reads float and prints price with discount

price = float(input("Digite o preço do produto: "))
discount = (price * 5) / 100
new_price = price - discount

print(
    "O produto custa R$ {:.2f}, com desconto de 5%, o produto custará: R$ {:.2f}.".format(
        price, new_price
    )
)
