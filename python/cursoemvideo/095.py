# Multiple players games registry
jogador = {}
partidas = []
time = []
while True:
	jogador['nome'] = str(input('Nome do Jogador: '))
	total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
	jogador['total'] = sum(partidas)

	c = 1
	while c <= total_partidas:
		jogador['jogos'] = c
		partidas.append(int(input(f'Quantos gols na partida {c}? ')))

		c += 1
	jogador['gols'] = partidas[:]
	jogador['total'] = sum(partidas)
	time.append(jogador.copy())
	while True:
		resposta = str(input('Deseja continuar? [S/N] ').strip().upper()[0])
		if resposta in 'SN':
			break
		print('ERRO! Por favor, digite S ou N.')
	if resposta == 'N':
		break
print(time)
flourish = ('-=' * 32)
print(flourish)

while True:
	qual_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
	if qual_jogador == 999:
		print('>>>PROGRAMA ENCERRADO<<<')
		break
	if qual_jogador not in range(0, len(time)):
		print(f'ERRO! Não existe jogador com o código {qual_jogador}!' )
		continue
	print(time[qual_jogador])
