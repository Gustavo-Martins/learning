"""Draw numbers and sum evens."""
from random import randint
from time import sleep


def draw_num(list):
    """Randomly draws 5 values from list."""
    print("Sorteando 5 valores da lista: ", end="")
    for i in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print("PRONTO!")


def even_sum(list):
    """Adds numbers from list."""
    even_total = 0
    for n in list:
        if n % 2 == 0:
            even_total += n
    print(f"Somando os valores pares de {list}, temos {even_total}.")


numbers = []
draw_num(numbers)
even_sum(numbers)
