# Reads int and converts to binary, octal or hexadecimal.
number = int(input('Digite um número inteiro: '))
print('Escolha uma das seguintes bases para conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
option = int(input('Sua opção: '))

if option == 1:
   print('{} em binário é: {}'.format(number, bin(number)[2:])) 
elif option == 2:
    print('{} em octal é: {}'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} em hexadecimal é: {}'.format(number, hex(number)[2:]))
else:
    print('Digite uma opção válida.')
