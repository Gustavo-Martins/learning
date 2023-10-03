# Military conscription checker
from datetime import date

birth_year = int(input("Por favor, digite o seu ano de nascimento: "))
current_year = date.today().year
age = current_year - birth_year

if age < 18:
    print("Jovem, ainda faltam {} anos para o seu ano de alistamento.".format(18 - age))
elif age > 18:
    print(
        "Jovem, o Brasil te aguarda há {} anos pelo seu alistamento.".format(age - 18)
    )
else:
    print(
        """Jovem, está no seu ano de servir ao Brasil,
    apresente-se no posto de alistamento mais próximo."""
    )
