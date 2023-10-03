def check(msg):
    """ "Checks if user input is a valid price."""
    valid = False
    while not valid:
        usr_input = str(input(msg)).replace(",", ".").strip()
        print(f"Verificando {usr_input}")
        if usr_input.isalpha() or usr_input == "":
            print(f'ERRO "{usr_input}" é um preço inválido.')
        else:
            valid = True
            return float(usr_input)


def read_int(msg):
    """Validates if input is a float."""
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print("\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[0;31mUsuário preferiu não informar um número.\033[m")
            return 0
        else:
            return n
            break


def read_float(msg):
    """Validates if input is a float."""
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print("\033[0;31mERRO! Por favor, digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[0;31mUsuário preferiu não informar um número.\033[m")
            return 0
        else:
            return n
            break
