"""Matrix math."""
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
evens = 0

flourish = "-=" * 30
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matrix[l][c] % 2 == 0:
            evens += matrix[l][c]
print(flourish)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrix[l][c]:^5}]", end="")
    print()

third_column = matrix[0][2] + matrix[1][2] + matrix[2][2]
max = max(matrix[1][0], matrix[1][2])
print(flourish)
print(f"A soma dos valores pares é: {evens}.")
print(f"A soma dos valores da terceira coluna é {third_column}.")
print(f"O maior valor da segunda linha é {max}.")
