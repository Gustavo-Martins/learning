"""Reads numbers and inputs sum."""
n = count = sum_numbers = 0
n = int(input("Digite um número [999 para parar]: "))
while n != 999:
    sum_numbers += n
    count += 1
    n = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {count} números e a soma entre eles foi {sum_numbers}.")
