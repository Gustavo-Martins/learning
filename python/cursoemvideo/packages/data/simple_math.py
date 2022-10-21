def factorial(n):
	"""Returns the factorial of a number.
	"""
	f = 1
	for counter in range(1, n+1):
		f *= counter
	return f


def double(n):
	"""Returns the double value of a number.
	"""
	return n * 2


def triple(n):
	"""Returns the triple value of a mumber.
	"""
	return n * 3
