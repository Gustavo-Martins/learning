"""Reads word list and print vowels;."""
words = (
    "APRENDER",
    "PROGRAMAR",
    "LINGUAGEM",
    "PYTHON",
    "CURSO",
    "GRATIS",
    "ESTUDAR",
    "PRATICAR",
    "TRABALHAR",
    "MERCADO",
    "PROGRAMADOR",
    "FUTURO",
)

for pos in words:
    print(f"\nNa palavra {pos} temos ", end="")
    for letter in pos:
        if letter in "AEIOU":
            print(letter.lower(), end=" ")
