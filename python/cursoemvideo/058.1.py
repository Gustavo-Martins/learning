"""Improved guessing game."""
from random import randint
from time import sleep


print("Sou seu computador...")
sleep(0.5)
print("Acabei de pensar em um número entre 0 e 10.")
sleep(0.5)
print("Será que você consegue adivinhar qual é?")
rand = randint(0, 10)
guess = int(input("Qual é o seu palpite? "))
count = 1
while guess != rand:
    if guess > rand:
        guess = int(input("Menos! Tente outro palpite: "))
    elif guess < rand:
        guess = int(input("Mais! Tente outro palpite: "))
    count += 1
print(f"Acertou! Foram necessárias {count} tentativas para acertar.")
