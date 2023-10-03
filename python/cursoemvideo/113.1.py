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


number = read_float("Digite um número: ")
print(f"Você digitou o número: {number:.2f}")
