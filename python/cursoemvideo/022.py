"""Reads name and prints info."""

name = str(input("Digite o seu nome completo: "))
nospace = name.replace(" ", "")
div = name.split()

print(f"O seu nome em maiúsculas é: {name.upper()}")
print(f"O seu nome em minúsculas é: {name.lower()}")
print(f"O seu nome sem espaços é: {nospace}")
print(f"Número de caracteres sem espaço: {len(nospace)}")
print(f"O seu primeiro nome é: {div[0]}")
print(f"O seu primeiro nome tem {len(div[0])} letras.")
