# Calculates rented car total fee

days = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

fee = (days * 60) + (km * 0.15)

print('O total a pagar é R$ {:.2f}.'.format(fee))
