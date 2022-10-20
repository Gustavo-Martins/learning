from calendar import c
from locale import currency


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
