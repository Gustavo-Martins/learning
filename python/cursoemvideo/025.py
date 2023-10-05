"""Gets input and searches for 'Silva'."""

name = input("Digite o seu nome: ").strip()

print(f"Seu nome tem Silva? {'silva' in name.lower()}")
