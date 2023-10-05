"""Larger integer evaluation."""
from time import sleep


def larger(*num):
    cont = 0
    larger = 0
    print("Analisando os valores passsados...")
    for n in num:
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
        if cont == 0:
            larger = n
        else:
            if n > larger:
                larger = n
        cont += 1
    sleep(0.5)
    print(f"Foram informados {cont} valores.")
    print(f"O maior valor informado foi {larger}.")
    print("-" * 20)


larger(2, 9, 4, 5, 7, 1)
larger(4, 7, 0)
larger(1, 2)
larger(6)
larger()
