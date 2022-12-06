# Package with menu building functions.
def flourish(size=35):
	"""Prints a string of '-'s."""
	print('-' * size)


def menu_header(txt):
	"""Prints menu header."""
	flourish()
	print(txt.center(35))
	flourish()


def menu_print_options(list):
	"""Prints main menu options list."""
	for item in list:
		n = 1
		print(f"{n} - {item}")
		n += 1
	flourish()


def menu_option(option):
	"""Prints selected main menu option."""
	txt = f"OPÇÃO {option}"
	flourish()
	print(txt.center(35))
	flourish()
