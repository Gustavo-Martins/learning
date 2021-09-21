# Validate mathematical expressions
stack = []
expr = str(input('Digite a expressão: '))
for simb in expr:
	if simb == '(':
		stack.append('(')

	elif simb == ')':
		if len(stack) > 0:
			stack.pop()
		else:
			stack.append(')')
			break
if len(stack) == 0:
	print('Sua expressão matemática é válida.')
else:
	print('Sua expressão matemática é inválida.')
