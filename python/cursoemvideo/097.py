"""Prints text."""


def write(txt):
    """Prints text."""
    length = len(txt) + 4
    print("-" * length)
    print(f"  {txt}")
    print("-" * length)


write("Gustavo Guanabara")
write("Curso de Python no YouTube")
write("CeV")
