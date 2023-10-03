# Rock, Papper, Scissors game
from random import randint
from time import sleep


print(
    """Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura"""
)
player = int(input("Qual a sua jogada? "))
if player in range(0, 3):
    computer = randint(0, 2)
    sleep(0.5)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(1)
    print("PO!")
    if player == computer:
        print("Nós fizemos a mesma jogada.")
        print("Empate!")
    elif player == 0 and computer == 2:
        print("Você jogou Pedra, e eu joguei Tesoura.")
        print("Você venceu!")
    elif player == 0 and computer == 1:
        print("Você jogou Pedra, e eu joguei Papel.")
        print("Você perdeu!")
    elif player == 1 and computer == 0:
        print("Você jogou Papel, e eu joguei Pedra.")
        print("Você venceu!")
    elif player == 1 and computer == 2:
        print("Você jogou Papel, e eu joguei Tesoura.")
        print("Você perdeu!")
    elif player == 2 and computer == 1:
        print("Você jogou Tesoura, e eu joguei Papel.")
        print("Você venceu!")
    elif player == 2 and computer == 0:
        print("Você jogou Tesoura, e eu joguei Pedra.")
        print("Você perdeu!")
else:
    print("Por favor, digite 0, 1 ou 2.")
