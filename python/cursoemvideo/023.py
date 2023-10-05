"""Reads number and outputs digits."""

number = int(input("Digite um numero de 0 a 9999: "))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print(f"O número {number} contém: ")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
