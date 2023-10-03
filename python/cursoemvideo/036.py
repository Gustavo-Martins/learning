# Loans approval checker
real_state_value = float(input("Valor da casa: R$ "))
wages = float(input("Salário do comprador: R$ "))
loan_duration = int(input("Quantos anos de financiamento? "))

montly_payment = real_state_value / (loan_duration * 12)
print(
    "Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.".format(
        real_state_value, loan_duration, montly_payment
    )
)

if montly_payment > (wages * 0.30):
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo pode ser CONCEDIDO!")
