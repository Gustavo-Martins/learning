from packages.interface.menu import menu_header


def create_file(name):
    try:
        # Try to open file, create if it doesn't exist.
        f = open(name, 'wt+')
        f.close()
    except:
        print('Ocorreu um erro na criação do arquivo.')
    else:
        print(f'Arquivo {name} criado com sucesso!')


def file_exists(name):
    try:
        # Try to open file in text mode.
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def read_file(name):
    try:
        # Try to read a text file
        f = open(name, 'rt')
    except:
        print('Ocorreu um erro ao ler o arquivo.')
    else:
        menu_header("PESSOAS CADASTRADAS")
        print(f.readlines())
