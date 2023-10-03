# Reads float and prints BRL money to EUR conversion
# In 2020/11/01 € 1.00 = R$ 6.69  :(

brl = float(input("Por favor, digite quanto dinheiro você tem na carteira: R$ "))
eur = brl / 6.69

print("Com R$ {:.2f} você pode comprar € {:.2f}.".format(brl, eur))
