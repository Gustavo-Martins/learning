"""Reads salary float value and prints value with 15% raise."""

salary = float(input("Digite o valor do seu salário: R$ "))

print(
    f"O seu salário foi aumentado de R$ {salary:.2f} para R$ {salary, salary + salary * 0.15:.2f}"
)
