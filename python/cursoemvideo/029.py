"""Reads speed value and prints if driver gets a ticket."""

speed = float(input("Qual a velocidade atual do carro? "))

if speed > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80 Km/h.")
    print(f"Você deve pagar uma multa de R$ {(speed - 80) * 7:.2f}!")

print("Tenha um bom dia! Dirija com segurança!")
