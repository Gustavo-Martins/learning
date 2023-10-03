from packages.currency.currency import format, decrement, double, half, increment


price = float(input("Digite o preço: "))
print(f"A metade de R$ {(price)} é R$ {(half(price))}.")
print(f"O triplo de R$ {(price)} é R$ {(double(price, True))}.")
print(f"Aumentando 20%, temos {(increment(price, 20, True))}.")
print(f"Reduzindo 13%, temos {(decrement(price, 13, True))}.")
