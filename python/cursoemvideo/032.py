# Prints if a date is a leap year
from datetime import date


year = int(input("Qual ano deseja analisar? Digite 0 para o ano atual: "))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("O ano {} é BISSEXTO.".format(year))
else:
    print("O ano {} NÃO É BISSEXTO.".format(year))
