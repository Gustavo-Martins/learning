# Reads salary float value and prints value with 15% raise

salary = float(input("Digite o valor do seu salário: R$ "))

print(
    "O seu salário foi aumentado de R$ {:.2f} para R$ {:.2f}.".format(
        salary, salary + salary * 0.15
    )
)
