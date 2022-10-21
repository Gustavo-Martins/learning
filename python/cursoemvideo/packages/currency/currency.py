# from calendar import c
# from locale import currency


def format(price, currency='R$', fmt=False):
	"""Returns price formatted as currency.
	"""
	return f'{currency} {price:>.2f}'.replace('.',',')


def decrement(n=0, percent=0, fmt=False):
	"""Returns n% decrement of n.
	"""
	rep = (n - (n * 1/percent))
	return rep if not fmt else format(rep)


def double(n=0, fmt=False):
	"""Returns double the value of n.
	"""
	rep = n * 2
	return rep if not fmt else format(rep)


def half(n=0, fmt=False):
	"""Returns half of a value n.
	"""
	rep = n / 2
	return rep if not fmt else format(rep)


def increment(n=0, percent=0, fmt=False):
	"""Returns n% increment of n.
	"""
	rep = (n + (n * 1/percent))
	return rep if not fmt else format(rep)


def summary(price, inc, dec):
	""""Summary of currency value operations.
	Keywords Arguments:
		price -- (float)
		inc -- (int) increment of price
		dec -- (int) decement of price
	Returns:
		Prints value formatted for currency, double the value,
		half the value,	% of increment, % of decrement.
	"""
	chars = 40
	flourish = ('-' * chars)
	print(flourish)
	print('RESUMO DO VALOR'.center(chars))
	print(flourish)
	print(f'Preço analisado: \t{format(price)}')
	print(f'Dobro do preço: \t{double(price, True)}')
	print(f'Metade do preço: \t{half(price, True)}')
	print(f'{inc}% de aumento: \t{increment(price, inc, True)}')
	print(f'{dec}% de aumento: \t{decrement(price, dec, True)}')
	print(flourish)
	