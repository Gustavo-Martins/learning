# Checks gender input
gender = str(input("Informe o seu gênero: [M/F] ").strip().upper()[0])
while gender not in "MF":
    gender = str(
        input("Dados inválidos. Por favor, informe o seu gênero: ").strip().upper([0])
    )
print("Gênero {} registrado com sucesso.".format(gender))
