"""Employees registry."""
from datetime import datetime


dados = {}
dados["nome"] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
dados["idade"] = datetime.now().year - nascimento
dados["ctps"] = int(input("Carteira de Trabalho (0 não possui): "))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("Ano de Contratação: "))
    dados["salário"] = float(input("Salário: R$ "))
    # Assuming 35 working years as default for retiring
    dados["aposentadoria"] = (
        dados["idade"] + (dados["contratação"] + 35) - datetime.now().year
    )
print("-=" * 30)
for k, v in dados.items():
    print(f" - {k} tem o valor {v}")
