dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valord = dias * 60
valorkm = km * 0.15
print(' O total a pagar é de {:.2f}' .format(valord + valorkm))