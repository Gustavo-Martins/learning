# Reads input and prints first and last name

name = str(input("Digite o seu nome completo: ")).split()

print("Prazer em conhecê-lo!")
print(name)
print("O seu primeiro nome é: {}".format(name[0]))
print(" O seu último nome é: {}".format(name[-1]))
