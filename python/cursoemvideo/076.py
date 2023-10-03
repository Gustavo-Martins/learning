# Items list
flourish = "-" * 39
items = (
    "Papel A4",
    0.25,
    "Papel A3",
    0.40,
    "Caderno",
    14.00,
    "Livro de Português",
    300.00,
    "Caneta",
    3.50,
    "Lapiseira",
    23.75,
    "Grafite",
    2.00,
)
print(flourish)
print("LISTAGEM DE PREÇOS")
print(flourish)
for pos in range(0, len(items)):
    if pos % 2 == 0:
        print(f"{items[pos]:.<30}", end="")
    else:
        print(f"R$ {items[pos]:>5.2f}")
print(flourish)
