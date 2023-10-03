from packages.currency.currency import decrement, double, half, increment


price = float(input("Digite o preço: "))
print(f"A metade de R$ {price} é R$ {half(price)}.")
print(f"O triplo de R$ {price} é R$ {double(price)}.")
print(f"Aumentando 10%, temos {increment(price, 10)}.")
print(f"Reduzindo 25%, temos {decrement(price, 25)}.")
