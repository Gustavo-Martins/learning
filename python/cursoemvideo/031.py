# Calculates trip ticket cost
distance = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {:.2f} Km.".format(distance))

if distance <= 200:
    print("E o preço da sua passagem será de R$ {:.2f}.".format(distance * 0.5))
else:
    print("E o preço da sua passagem será de R$ {:.2f}.".format(distance * 0.45))
