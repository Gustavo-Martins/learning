# Converts Celsius to Fahrenheit

celsius = float(input("Digite a temperatura (°C): "))
fahrenheit = celsius / 5 * 9 + 32

print("{:.1f} °C equivalem a {:.1f} °F.".format(celsius, fahrenheit))
