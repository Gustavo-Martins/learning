# Reads integer and prints basic math operations

numero = int(input('Digite um número inteiro para ver a sua tabuada: '))

def basicMath():
    i = 1
    for n in range(1, 11):
        print('{}'.format(numero * i))
        i += 1

basicMath()
