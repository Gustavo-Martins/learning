# Print student situation
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
	aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
	aluno['situação'] = 'Recuperação'
else:
	aluno['situação'] = 'Reprovado'
print('-=' * 15)
for k, v in aluno.items():
	print(f' - {k} é igual {v}')
