"""Prints Python libraries help."""
from time import sleep


colours = {
    "no_colour": "\033[m",
    "red": "\033[0;31;40m",
    "green": "\033[0;32;40m",
    "blue": "\033[0;34;40m",
    "white": "\033[37;40m",
}


def py_help(kwarg):
    """Displays function or library help files."""

    title(f"Acessando o manual do comando '{kwarg}'", "blue")
    sleep(1)
    help(kwarg)


def title(msg, c="no_colour"):
    """Colour picker for messages.
    Keyword arguments:
    msg -- string
    c -- default == 'no_colour' (optional) Colour to be printed to terminal.
    """
    size = len(msg) + 4
    print(colours[c], end="")
    print("~" * size)
    print(f"{msg}")
    print("~" * size)
    print(colours["no_colour"], end="")  # Removing the previous colour selection.


while True:
    option = ""
    title("Sistema de Ajuda PyHelp", c="red")
    option = str(input("Função ou Biblioteca: ").lower().strip())
    if option == "fim":
        sleep(0.5)
        title("Até logo!", "green")
        break
    else:
        py_help(option)
