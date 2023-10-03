from packages.currency.currency import format, decrement, double, half, increment


price = float(input("Digite o preço: "))
print(f"A metade de R$ {format(price)} é R$ {format(half(price))}.")
print(f"O triplo de R$ {format(price)} é R$ {format(double(price))}.")
print(f"Aumentando 10%, temos {format(increment(price, 10))}.")
print(f"Reduzindo 25%, temos {format(decrement(price, 25))}.")
