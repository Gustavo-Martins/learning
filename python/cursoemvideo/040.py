"""Reads two grades and prints average."""
grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
grade_average = (grade1 + grade2) / 2
print(f"Tirando {grade1:.1f} e {grade2:.1f}, a média é {grade_average:.1f}")

if grade_average < 5:
    print("O aluno(a) está REPROVADO")
elif grade_average >= 7:
    print("O aluno(a) está APROVADO")
else:
    print("O aluno(a) está em RECUPERAÇÃO")
