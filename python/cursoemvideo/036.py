"""Loans approval checker."""
real_state_value = float(input("Valor da casa: R$ "))
wages = float(input("Salário do comprador: R$ "))
loan_duration = int(input("Quantos anos de financiamento? "))

montly_payment = real_state_value / (loan_duration * 12)
print(
    f"Para pagar uma casa de R$ {real_state_value:.2f} em {loan_duration} anos, a prestação será de R$ {montly_payment:.2f}."
)

if montly_payment > (wages * 0.30):
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo pode ser CONCEDIDO!")
