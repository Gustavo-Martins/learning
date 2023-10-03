# Reads float and prints price with discount

price = float(input("Digite o preço do produto: R$ "))
new_price = price - (price * 5 / 100)

print(
    "O preço do produto é R$ {:.2f}, com desconto de 5%, custará R$ {}.".format(
        price, new_price
    )
)
