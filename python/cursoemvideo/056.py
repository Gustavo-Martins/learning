# Reads 4 person data and prints statistics
age_total = 0
age_average = 0
oldest = 0
young_women = 0

for person in range(1, 5):
    print("-----{}ª----- pessoa".format(person))
    name = str(input("Nome: ")).strip()
    age = int(input("Idade: "))
    age_total += age
    gender = str(input("Sexo [M/F]: ")).strip().upper()
    if person == 1 and gender == "M":
        oldest = age
        elder = name
    if gender == "M":
        if age > oldest:
            oldest = age
            elder = name
    if gender == "F" and age < 20:
        young_women += 1

age_average = age_total / 4

print("A idade do homem mais velho é {} anos, e seu nome é {}.".format(oldest, elder))
print("A média de idade do grupo é de {:.1f} anos.".format(age_average))
print("Ao todo {} mulheres tem menos de 20 anos.".format(young_women))
