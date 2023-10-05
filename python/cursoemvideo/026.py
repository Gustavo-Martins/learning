"""Gets input and prints 'A' occurences and position."""

text = str(input("Digite o texto: ")).lower().strip()

print(text)
print(f"A letra 'A' aparece {text.count('a')} vezes no texto.")
print(f"A letra 'A' aparece pela primeira vez na posição {text.find('a') + 1}")
print(f"A letra 'A' aparece pela última vez na posição {text.rfind('a') + 1}")
