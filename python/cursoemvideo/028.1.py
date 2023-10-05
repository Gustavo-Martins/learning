"""Guessing game."""
from random import randint
from time import sleep


computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")
