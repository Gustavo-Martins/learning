list = []


def add_number(numero):
    list.append(numero)


def remove_queue():
    list.pop(0)


def remove_stack():
    list.pop()


def print_list():
    print(list)


while True:
    option = str(
        input("Qual estrutura deseja utilizar (Pilha, Fila ou Sair)? ").lower()
    )
    if option == "pilha":
        print("Você escolheu Pilha.")
        while True:
            sel_function = str(
                input("Adicionar número, Remover número, ou Sair? ").lower()
            )
            if sel_function == "adicionar":
                numero = int(input("Digite o número a ser adicionado: "))
                add_number(numero)
                print_list()
            elif sel_function == "remover":
                if len(list) > 0:
                    remove_stack()
                    print_list()
                else:
                    print("Não é possível remover números de uma pilha vazia.")
            elif sel_function == "sair":
                print("Retornando ao menu principal...")
                list.clear()
                break
            else:
                print("Por favor, digite uma opção válida.")
    elif option == "fila":
        print("Você escolheu Fila.")
        while True:
            sel_function = str(
                input("Adicionar número, Remover número, ou Sair? ").lower()
            )
            if sel_function == "adicionar":
                numero = int(input("Digite o número a ser adicionado: "))
                add_number(numero)
                print_list()
            elif sel_function == "remover":
                if len(list) > 0:
                    remove_queue()
                    print_list()
                else:
                    print("Não é possível remover números de uma fila vazia.")
            elif sel_function == "sair":
                print("Retornando ao menu principal...")
                list.clear()
                break
            else:
                print("Por favor, digite uma opção válida.")
    elif option == "sair":
        print("Encerrando programa...")
        break
    else:
        print("Por favor, selecione uma opção válida.")
