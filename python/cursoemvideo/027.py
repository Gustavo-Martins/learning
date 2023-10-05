"""Reads input and prints first and last name."""

name = str(input("Digite o seu nome completo: ")).split()

print("Prazer em conhecê-lo!")
print(name)
print(f"O seu primeiro nome é: {name[0]}")
print(f"O seu último nome é: {name[-1]}")
