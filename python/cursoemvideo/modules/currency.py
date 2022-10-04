def format(price, currency = 'R$'):
	"""Returns price formatted as currency.
	"""
	return f'{currency} {price:>.2f}'.replace('.',',')


def decrement(n = 0, percent = 0):
	"""Returns n% decrement of n.
	"""
	return (n - (n * 1/percent))


def double(n = 0):
	"""Returns double the value of n.
	"""
	return n * 2


def half(n = 0):
	"""Returns half of a value n.
	"""
	return n / 2


def increment(n = 0, percent = 0):
	"""Returns n% increment of n.
	"""
	return (n + (n * 1/percent))
