"""Reads float and prints BRL money conversion to USD."""
# In 2020/11/01 US$1.00 = R$ 5.74  :(

brl = float(input("Por favor, digite quanto dinheiro você tem na carteira: R$ "))
usd = brl / 5.74

print(f"Com R$ {brl:.2f} você pode comprar US$ {usd:.2f}.".format(brl, usd))
