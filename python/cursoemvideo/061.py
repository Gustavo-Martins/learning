# Prints arithmetic progression of 10 numbers
print("Gerador de PA")
print("-=-" * 10)
first = int(input("Primeiro termo:  "))
constant = int(input("Razão da PA: "))
number = first
counter = 1
while counter <= 10:
    print("{}".format(number), end=" → ")
    number += constant
    counter += 1
print("FIM")
