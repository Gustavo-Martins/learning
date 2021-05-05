# Reads two grades and prints average
grade1 = float(input('Digite a primeira nota: '))
grade2 = float(input('Digite a segunda nota: '))
grade_average = (grade1 + grade2) / 2
print('Tirando {:.1f} e {:.1f}, a média é {:.1f}'.format(grade1, grade2, grade_average))

if grade_average < 5:
    print('O aluno(a) está REPROVADO')
elif grade_average >= 7:
    print('O aluno(a) está APROVADO')
else:
    print('O aluno(a) está em RECUPERAÇÃO')
