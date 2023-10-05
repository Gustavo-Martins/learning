"""Military conscription age checker."""
from datetime import date

birth_year = int(input("Por favor, digite o seu ano de nascimento: "))
current_year = date.today().year
age = current_year - birth_year

if age < 18:
    print(f"Jovem, ainda faltam {18 - age} anos para o seu ano de alistamento.")
elif age > 18:
    print(f"Jovem, o Brasil te aguarda há {age - 18} anos pelo seu alistamento.")
else:
    print(
        """Jovem, está no seu ano de servir ao Brasil,
    apresente-se no posto de alistamento mais próximo."""
    )
