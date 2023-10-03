# Reads name and prints info

name = str(input("Digite o seu nome completo: "))
nospace = name.replace(" ", "")
div = name.split()

print("O seu nome em maiúsculas é: {}".format(name.lower()))
print("O seu nome em minúsculas é: {}".format(name.upper()))
print("O seu nome sem espaços é: {}".format(nospace))
print("Número de caracteres sem espaço: {}".format(len(nospace)))
print("O seu primeiro nome é: {}".format(div[0]))
print("O seu primeiro nome tem {} letras.".format(len(div[0])))
