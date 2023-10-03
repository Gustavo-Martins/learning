# Prints sum
count = sum = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    count += 1
    sum += n
print(f"A soma dos {count} valores foi {sum}!")
