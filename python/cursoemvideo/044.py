"""Total purchase value calculator."""
print(f"{' LOJAS GLAMAZON ':=^40}")
subtotal = float(input("Digite valor da sua compra: "))
payment_method = float(
    input(
        """Selecione a forma de pagamento: 
                            [1] à vista no dinheiro ou cheque;
                            [2] à vista no cartão;
                            [3] 2x no cartão;
                            [4] 3x ou mais no cartão.\n"""
    )
)

if payment_method == 1:
    total = subtotal - (subtotal * 0.10)
    print(f"O preço final da compra de R$ {subtotal:.2f} será: R$ {total:.2f}")
elif payment_method == 2:
    total = subtotal - (subtotal * 0.05)
    print(f"O preço final da compra de R$ {subtotal:.2f} será: R$ {total:.2f}")
elif payment_method == 3:
    print("Não serão aplicados descontos ou juros na sua compra.")
    print(f"O preço final da sua compra será compra de R$ {subtotal:.2f}")
elif payment_method == 4:
    n_monthly_payments = int(input("Digite o número de parcelas: "))
    if n_monthly_payments < 3:
        print("Por favor, selecione pelo menos 3 parcelas.")
    else:
        monthly_payment_value = float(subtotal / n_monthly_payments)
        total = subtotal - (subtotal * 0.20)
        print(
            f"Sua compra será parcelada em {n_monthly_payments}x de R$ {monthly_payment_value:.2f} com juros."
        )
        print(f"O preço final da sua compra de R$ {subtotal:.2f} será: R$ {total:.2f}")
else:
    print("Por favor, selecione uma forma de pagamento válida.")
