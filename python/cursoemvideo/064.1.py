# Reads numbers and inputs sum
n = count = sum = 0
n = int(input("Digite um número [999 para parar]: "))
while n != 999:
    sum += n
    count += 1
    n = int(input("Digite um número [999 para parar]: "))
print("Você digitou {} números e a soma entre eles foi {}.".format(count, sum))
