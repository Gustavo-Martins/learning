"""Gets input and prints previous and next number."""

number = int(input("Digite um número inteiro: "))

print(
    "O seu número digitado é {}, o anterior é {}, e o próximo é {}".format(
        number, (number - 1), (number + 1)
    )
)
