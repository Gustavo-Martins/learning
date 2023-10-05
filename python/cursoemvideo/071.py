"""ATM simulator."""
flourish = "=" * 40

print(flourish)
print("{:^40}".format("BANCO CEV"))
print(flourish)

withdrawal = int(input("Quanto você quer sacar? "))
total = withdrawal
bill = 50
total_bills = 0

while True:
    if total >= bill:
        total -= bill
        total_bills += 1
    else:
        if total_bills > 0:
            print(f"Total de {total_bills} cédulas de R$ {bill}")
        if bill == 50:
            bill = 20
            total_bills = 0
        elif bill == 20:
            bill = 10
            total_bills = 0
        elif bill == 10:
            bill = 1
        total_bills = 0
        if total == 0:
            break

print(flourish)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
