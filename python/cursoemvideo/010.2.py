# Reads float and prints BRL money conversion to JPY
# In 2020/11/01 JP¥ 1.00 = R$ 0.060  :)

brl = float(input("Por favor, digite quanto dinheiro você tem na carteira: R$ "))
jpy = brl / 0.060

print("Com R$ {:.2f} você pode comprar ¥ {:.2f}.".format(brl, jpy))
