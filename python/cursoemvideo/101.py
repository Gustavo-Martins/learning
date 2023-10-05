"""Voting age checks."""
from datetime import date


def vote(year=0):
    """Checks voting rights by age, returns classification.

    Keyword arguments:
    year -- default == 0
    """
    age = date.today().year - year
    if age < 16:
        return f"Com {age} anos: Não Vota"
    elif 16 <= age < 18 or age > 70:
        return f"Com {age} anos: Voto Facultativo"
    else:
        return f"Com {age} anos: Voto Obrigatório"


print("-" * 30)
year = int(input("Em que ano você nasceu? "))
print(vote(year))
