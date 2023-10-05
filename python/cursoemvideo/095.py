"""Multiple players games registry."""
jogador = {}
partidas = []
time = []
while True:
    jogador["nome"] = str(input("Nome do Jogador: "))
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    jogador["total"] = sum(partidas)

    c = 1
    while c <= total_partidas:
        jogador["jogos"] = c
        partidas.append(int(input(f"Quantos gols na partida {c}? ")))
        c += 1
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = str(input("Deseja continuar? [S/N] ").strip().upper()[0])
        if resposta in "SN":
            break
        print("ERRO! Por favor, digite S ou N.")
    if resposta == "N":
        break
flourish = "-=" * 32

print("-" * 40)
print("cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
for k, v in enumerate(time):
    print(f"{k:>4}", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-" * 40)
while True:
    qual_jogador = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if qual_jogador == 999:
        print(">>>PROGRAMA ENCERRADO<<<")
        break
    if qual_jogador not in range(0, len(time)):
        print(f"ERRO! Não existe jogador com o código {qual_jogador}!")
        continue
    else:
        print(f'  -- Levantamento do Jogador: {time[qual_jogador]["nome"]}')
    print(flourish)
    for i, g in enumerate(time[qual_jogador]["gols"]):
        print(f'    +> Na partida {i+1}, {time[qual_jogador]["nome"]} fez {g} gols.')
    print(
        f'O jogador {time[qual_jogador]["nome"]} jogou {len(time[qual_jogador]["gols"])} partidas.'
    )
    print(f'Foi um total de {time[qual_jogador]["total"]} gols.')
    print(flourish)
