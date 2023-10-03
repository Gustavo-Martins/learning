def read_float(msg):
    """Validates if input is a float."""
    while True:
        try:
            n = float(input(msg))
        except:
            print("\033[0;31mERRO! Por favor, digite um número real válido.\033[m")
        else:
            break
    return n


number = read_float("Digite um número: ")
print(f"Você digitou o número: {number:.2f}")
