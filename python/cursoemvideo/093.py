# Players games registry
jogador = {}
partidas = []
jogador["nome"] = str(input("Nome do Jogador: "))
total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador["total"] = sum(partidas)

c = 1
while c <= total_partidas:
    jogador["jogos"] = c
    partidas.append(int(input(f"Quantos gols na partida {c}? ")))

    c += 1
jogador["gols"] = partidas[:]
jogador["total"] = sum(partidas)

flourish = "-=" * 32
print(flourish)
print(jogador)
print(flourish)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print(flourish)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f"    => Na partida {i+1}, fez {v} gols.")
print(f'Total de gols: {jogador["total"]}')
