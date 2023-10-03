# Stores and displays students grades
grades = list()
flourish = "=-" * 15

while True:
    name = str(input("Nome: "))
    grade1 = float(input("Nota 1: "))
    grade2 = float(input("Nota 2: "))
    average = (grade1 + grade2) / 2
    grades.append([name, [grade1, grade2], average])
    print(grades)
    choice = str(input("Quer continuar? [S/N] ")).strip().lower()
    if choice == "n":
        break
print(flourish)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(flourish)
for i, s in enumerate(grades):
    print(f"{i:<4}{s[0]:<10}{s[2]:>8.1f}")
while True:
    print(flourish)
    student = int(input("Mostrar as notas de qual estudante? (999 interrompe) "))
    if student == 999:
        print("FINALIZANDO...")
        break
    if student <= len(grades) - 1:
        print("-" * 31)
        print(f"Notas de {grades[student][0]} são: {grades[student][1]}")
print("VOLTE SEMPRE")
