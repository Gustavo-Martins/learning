"""Reads numbers and prints sum."""
n = 0
sum_numbers = 0
numbers = 0

while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        sum_numbers += n
        numbers += 1
print(f"Você digitou {numbers} números e a soma entre eles foi {sum_numbers}.")
