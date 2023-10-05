"""Calculator with menu."""
from time import sleep


x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
choice = 0
while choice in range(0, 5):
    print(
        """
	[1] somar
	[2] multiplicar
	[3] maior
	[4] novos números
	[5] sair do programa
	"""
    )
    choice = int(input("Qual é a sua opção? "))

    if choice == 1:
        print(f"A soma de {x} e {y} é: {x + y:.2f}")
    elif choice == 2:
        print(f"O produto de {x} e {y} é: {x * y:.2f}")
    elif choice == 3:
        if x > y:
            print(f"{x} é maior que {y}.")
        if x < y:
            print("{x} é maior que {y}.")
        if x == y:
            print("Os dois números são iguais.")
    elif choice == 4:
        print("Informe os números novamente.")
        x = float(input("Digite o primeiro valor: "))
        y = float(input("Digite o segundo valor: "))
    elif choice == 5:
        sleep(0.5)
        print("Finalizando...")
        quit()
    else:
        print("Opção inválida, por favor, digite um número entre 1 e 5.")
