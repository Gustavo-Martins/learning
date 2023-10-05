"""Football players goals registry."""


def register(p="<desconhecido>", g=0):
    print(f"O jogador {p} fez {g} gols.")


player = str(input("Nome do Jogador: "))
goals = str(input("Número de Gols: "))

if goals.isnumeric():
    g = int(goals)
else:
    goals = 0
if player.strip() == "":
    register(g=goals)
else:
    register(player, goals)
