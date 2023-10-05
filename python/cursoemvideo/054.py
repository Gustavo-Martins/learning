"""Reads 7 ages and prints how many are above the age of majority."""
from datetime import date


current_year = date.today().year
birthyear = 0
adult = 0
minor = 0

for person in range(1, 8):
    birthyear = int(input(f"Em que ano a {person}ª pessoa nasceu? "))
    age = current_year - birthyear
    if age >= 21:
        adult += 1
    else:
        minor += 1

print(f"{adult} pessoas são adultas, e {minor} pessoas são menores de idade.")
