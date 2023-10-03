# Classify swimmers by birth_year
from datetime import date

current_year = date.today().year
birth_year = int(input("Digite o ano de nascimento do(a) atleta: "))
age = current_year - birth_year

print("O(a) atleta tem {} anos, e pertence à categoria:".format(age))
if age <= 9:
    print("MIRIM")
elif age <= 14:
    print("INFANTIL")
elif age <= 19:
    print("JÚNIOR")
elif age <= 25:
    print("SÊNIOR")
elif age > 25:
    print("MASTER")
