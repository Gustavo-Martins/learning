# People registry and age average
person = {}
registry = []
choice = " "
age_sum = 0
average_age = 0
while True:
    person.clear()
    person["name"] = str(input("Nome: "))
    person["sex"] = str(input("Sexo: [M/F] ").strip().upper()[0])
    while person["sex"] not in "MF":
        print("ERRO! Por favor, digite apenas M ou F.")
        person["sex"] = str(input("Sexo: [M/F] ").strip().upper()[0])
    person["age"] = int(input("Idade: "))
    age_sum += person["age"]
    registry.append(person.copy())
    while True:
        choice = str(input("Quer continuar? [S/N] ").strip().upper()[0])
        if choice in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if choice == "N":
        break


print("-=" * 30)
print(f"Ao todo foram cadastradas {len(registry)} pessoas.")
average_age = age_sum / len(registry)
print(f"A média de idade é de {average_age} anos.")
print("As mulheres cadastradas foram ", end="")
for person in registry:
    if person["sex"] in "F":
        print(f'{person["name"]}', end=", ")
print()
print("Lista das pessoas com idade acima da média: ")
for person in registry:
    if person["age"] > average_age:
        print(f'{person["name"]}', end=", ")
