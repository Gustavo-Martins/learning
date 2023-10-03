# Reads number and outputs digits

number = int(input("Digite um numero de 0 a 9999: "))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print("O número {} contém: ".format(number))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))
