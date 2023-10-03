# Calculator with menu
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
        print("A soma de {} e {} é: {:.2f}".format(x, y, (x + y)))
    elif choice == 2:
        print("O produto de {} e {} é: {:.2f}".format(x, y, (x * y)))
    elif choice == 3:
        if x > y:
            print("{} é maior que {}.".format(x, y))
        if x < y:
            print("{} é maior que {}.".format(y, x))
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
