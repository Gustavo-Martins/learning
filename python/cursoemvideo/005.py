# Gets input and prints previous and next number

number = int(input("Digite um número inteiro: "))
previous_number = number - 1
next_number = number + 1

print(
    "O seu número digitado é {}, o anterior é {}, e o próximo é {}.".format(
        number, previous_number, next_number
    )
)
