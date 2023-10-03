# Reads numbers and prints sum
n = 0
sum = 0
numbers = 0

while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        sum += n
        numbers += 1
print("Você digitou {} números e a soma entre eles foi {}.".format(numbers, sum))
