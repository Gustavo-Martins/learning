# Gets input and searches for 'Silva'

name = input('Digite o seu nome: ').strip()

print('Seu nome tem Silva? {}'.format('silva' in name.lower()))
