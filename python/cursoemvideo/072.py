# Prints numerals
numerals = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if n in range(0, 21):
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número: {numerals[n]}")
