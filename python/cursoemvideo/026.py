# Gets input and prints 'A' occurences and position

text = str(input("Digite o texto: ")).lower().strip()

print(text)
print('A letra "A" aparece {} vezes no texto.'.format(text.count("a")))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(text.find("a") + 1))
print('A letra "A" aparece pela última vez na posição {}.'.format(text.rfind("a") + 1))
