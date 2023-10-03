# Reads input in metres and prints conversion to others distance units

metre = float(input("Digite um valor em metros: "))

millimetre = metre * 1000
centimetre = metre * 100
decimetre = metre * 10
decametre = metre * 0.01
hectometre = metre * 0.1
kilometre = metre * 0.001

print("{:.2f} metros equivalem a:".format(metre))
print(
    "{:.2f} milímetros \n{:.2f} centímetros \n{:.2f} decímetros".format(
        millimetre, centimetre, decimetre
    )
)
print(
    "{:.2f} decâmetros \n{:.2f} hectômetros \n{:.2f} quilômetros".format(
        decametre, hectometre, kilometre
    )
)
