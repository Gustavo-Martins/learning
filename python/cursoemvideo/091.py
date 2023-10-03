# Dice rolls and ranking
from operator import itemgetter
from random import randint
from time import sleep


game = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}
print("Valores sorteados:")
ranking = []
for k, v in game.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.5)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
sleep(1)
print("-=" * 32)
print("Classificação dos Jogadores")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(0.5)
