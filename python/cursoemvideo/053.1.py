"""Reads input, prints inverted and if it is a palindrome."""
phrase = str(input("Digite uma frase: ")).strip().upper()
words = phrase.split()
joined = "".join(words)
inverted = joined[::-1]
print(f"A frase {joined} invertida é: {inverted}")

if inverted == joined:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
