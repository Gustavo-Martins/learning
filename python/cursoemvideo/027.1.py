"""Reads name prints first and last name."""

n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[len(nome) - 1]}")
