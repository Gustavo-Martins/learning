# BMI calculator
weight = float(input("Qual o seu peso: (Kg) "))
height = float(input(" Qual a sua altura: (m) "))

imc = weight / (height**2)
print("O seu IMC é: {:.1f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso normal.")
elif imc < 25:
    print("Você está no peso ideal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 40:
    print("Você está obeso.")
elif imc >= 40:
    print("Você está em obesidade mórbida.")
