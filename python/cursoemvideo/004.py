"""Prints user input information."""

user_input = input("Digite algo: ")

print("O tipo primitivo é: ", type(user_input))
print("Só tem espaços: ", user_input.isspace())
print("É um número?", user_input.isnumeric())
print("É alfabético?", user_input.isalpha())
print("É alfanumérico?", user_input.isalnum())
print("Está em maiúsculas?", user_input.isupper())
print("Está em minúsculas?", user_input.islower())
print("Está capitalizada?", user_input.istitle())
