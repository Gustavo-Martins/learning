# Reads integer and prints basic math operations


def inputInteger(number):
    while True:
        try:
            number = int(input(number))
        except:
            print("Por favor, digite um número inteiro.")
        else:
            return number


numero = inputInteger("Digite um número inteiro para ver a sua tabuada: ")


def basicMath():
    i = 1
    inputInteger(numero)
    print("Número recebido {}".format(numero))
    for n in range(1, 11):
        print("Teste")
        print("{}".format(numero * i))
        i += 1


# print('{}'.format(numero))
basicMath()
