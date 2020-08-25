# Prints user input type

user_input = input('Digite algo: ')

if user_input.isspace() == True:
    print('Contém apenas espaços em branco.')
elif user_input.isdigit() == True:
    print('É um dígito.')
elif user_input.istitle() == True:
    print('É capitalizado.')
elif user_input.isalnum() == True:
    print('É alfabético.')
elif user_input.isnumeric() == True:
    print('É numérico.')
elif user_input.isalpha() == True:
    print('É alfanumérico')
elif user_input.isupper() == True:
    print('É caixa alta.')
elif user_input.islower() == True:
    print('É caixa baixa.')
elif user_input.isdigit() == True:
    print('É um dígito.')
else:
    print('Não foi possível classificar a sua entrada.')