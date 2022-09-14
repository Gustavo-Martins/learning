def grades(*args, classification=False):
	"""Receives grades, returns max, min, average and classification.
	Keywords Arguments:
	args -- (optional) Accepts multiples values of grades.
	classification -- (default=False) Classification of class grades (good, ok, bad).
	"""
	dict_grades = {}
	dict_grades['total'] = len(args)
	dict_grades['maior'] = max(args)
	dict_grades['menor'] = min(args)
	dict_grades['média'] = average = sum(args)/len(args)
	
	if classification:
		if average >= 7:
			dict_grades = 'Boa'
		elif average >= 5:
			dict_grades = 'Razoável'
		else:
			dict_grades = 'Ruim'
	return dict_grades


reply = grades(5, 9, 7, 4, classification=True)
print(reply)
# help(grades)
