# Price classification
cheapest = " "
count = expensive_item = total = 0
flourish = "-" * 15
while True:
    print(flourish)
    print("SUPERMERCADO TABAJARAS")
    print(flourish)
    item = str(input("Nome do Produto: "))
    price = float(input("Preço: R$ "))
    total += price
    count += 1
    if count == 1 or price < min:
        min = price
        cheapest = item
    if price > 1000:
        expensive_item += 1
    choice = " "
    while choice not in "sn":
        choice = str(input("Quer continuar? [S/N] ").strip().lower()[0])
    if choice == "n":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))
print(f"O total da compra foi R$ {total:.2f}")
print(f"Temos {expensive_item} produtos custando mais de R$ 1000.00")
print(f"O produto mais barato foi {cheapest} que custa R$ {min:.2f}")
