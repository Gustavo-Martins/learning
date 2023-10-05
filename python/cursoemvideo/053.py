"""Reads input, prints inverted and if it is a palindrome."""
phrase = str(input("Digite uma frase: ")).strip().upper()
words = phrase.split()
joined = "".join(words)
inverted = ""

for letter in range(len(joined) - 1, -1, -1):
    inverted += joined[letter]
print(f"A sua frase: \n{phrase}")
print(f"Invertida: \n{inverted}")

if inverted == joined:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
