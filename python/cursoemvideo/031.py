"""Calculates trip ticket cost."""
distance = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distance:.2f} Km.")

if distance <= 200:
    print(f"E o preço da sua passagem será de R$ {distance:.2f}.")
else:
    print(f"E o preço da sua passagem será de R$ {distance * 0.45:.2f}.")
