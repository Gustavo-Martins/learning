"""Reads int and converts to binary, octal or hexadecimal."""
number = int(input("Digite um número inteiro: "))
print("Escolha uma das seguintes bases para conversão:")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")
option = int(input("Sua opção: "))

if option == 1:
    print(f"{number} em binário é: {bin(number)[2:]}")
elif option == 2:
    print(f"{number} em octal é: {oct(number)[2:]}")
elif option == 3:
    print(f"{number} em hexadecimal é: {hex(number)[2:]}")
else:
    print("Digite uma opção válida.")
