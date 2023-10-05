"""Reads input in metres and prints conversion to others distance units."""

metre = float(input("Digite um valor em metros: "))

millimetre = metre * 1000
centimetre = metre * 100
decimetre = metre * 10
decametre = metre * 0.01
hectometre = metre * 0.1
kilometre = metre * 0.001

print(f"{metre:.2f} metros equivalem a:".format(metre))
print(
    f"{millimetre:.2f} milímetros \n{centimetre:.2f} centímetros \n{decimetre:.2f} decímetros"
)
print(
    f"{decametre:.2f} decâmetros \n{hectometre:.2f} hectômetros \n{kilometre:.2f} quilômetros"
)
