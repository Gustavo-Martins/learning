def grades(*args, classification=False):
    """Receives grades, returns max, min, average and classification.
    Keywords Arguments:
    args -- (optional) Accepts multiples values of grades.
    classification -- (default=False) Classification of class grades (good, ok, bad).
    """
    dict_grades = {args}
    average = sum(args) / len(args)
    print(f"Dicionário: {dict_grades}")
    print(f"Quantidade de notas: {len(args)}")
    print(f"Somatório das notas: {sum(args)}")
    print(f"Maior nota: {min(args)}")
    print(f"Menor nota: {max(args)}")
    print(f"Média de notas: {average}")

    if classification:
        if average >= 7:
            dict_grades = "Boa"
        elif average >= 5:
            dict_grades = "Razoável"
        else:
            dict_grades = "Ruim"
    return dict_grades


reply = grades(5, 9, 7, 4, classification=True)
print(reply)
# help(grades)
