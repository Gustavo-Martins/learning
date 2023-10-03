lista = []


def Adicionar(numero):
    lista.append(numero)


def RemoverPilha():
    lista.pop()


def RemoverFila():
    lista.pop(0)


def MostraLista():
    print(lista)


while True:
    seleciona = str(input("Digite uma opção: Pilha, Fila, Sair: ").strip().lower()[0])
    print(seleciona)
    if seleciona == "p":
        print("Selecionou Pilha")
        while True:
            sel_funcao = str(
                input("Digite Adicionar, Remover, Sair: ").strip().lower()[0]
            )
            if sel_funcao == "a":
                print("Selecionou Adicionar")
                numero = int(input("Digite o número a ser adicionado: "))
                Adicionar(numero)
                MostraLista()
            elif sel_funcao == "r":
                if len(lista) > 0:
                    print("Selecionou Remover")
                    RemoverPilha()
                    MostraLista()
                else:
                    print("Não é possível remover um número de uma pilha vazia.")
            elif sel_funcao == "s":
                print("Retornando ao menu principal...")
                break
            else:
                print("Por favor, digite uma opção válida.")
    elif seleciona == "f":
        print("Selecionou Fila")
        while True:
            sel_funcao = str(
                input("Digite Adicionar, Remover, Sair: ").strip().lower()[0]
            )
            if sel_funcao == "a":
                print("Selecionou Adicionar")
                numero = int(input("Digite o número a ser adicionado: "))
                Adicionar(numero)
                MostraLista()
            elif sel_funcao == "r":
                print("Selecionou Remover")
                if len(lista) > 0:
                    RemoverFila()
                    MostraLista()
                else:
                    print("Não é possível remover um número de uma fila vazia.")
            elif sel_funcao == "s":
                print("Retornando ao menu principal...")
                break
            else:
                print("Por favor, digite uma opção válida.")
    elif seleciona == "s":
        print("Encerrando o programa...")
        break
    else:
        print("Por favor, digite uma opção válida.")
