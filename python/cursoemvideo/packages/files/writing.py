from packages.interface.menu import menu_header


def create_file(name):
    try:
        # Try to open file, create if it doesn't exist.
        f = open(name, "wt+")
        f.close()
    except:
        print("Ocorreu um erro na criação do arquivo.")
    else:
        print(f"Arquivo {name} criado com sucesso!")


def file_exists(name):
    try:
        # Try to open file in text mode.
        f = open(name, "rt")
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def read_file(name):
    try:
        # Try to read a text file
        f = open(name, "rt")
    except:
        print("Ocorreu um erro ao ler o arquivo.")
    else:
        menu_header("PESSOAS CADASTRADAS")
        for row in f:
            data = row.split(";")
            data[1] = data[1].replace("\n", "")
            print(f"{data[0]:<30}{data[1]:>3} anos")
        # print(f.readlines())
    finally:
        f.close()


def write_to_file(file, name="desconhecido", age=0):
    try:
        # Try to append data to text file
        f = open(file, "at")
    except:
        print("Ocorreu um erro na abertura do arquivo.")
    else:
        try:
            f.write(f"{name};{age}\n")
        except:
            print("Ocorreu um erro ao salvar para o arquivo.")
        else:
            print(f"Novo registro de {name} adicionado.")
            f.close()
