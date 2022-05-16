def area(l, a):
    area = l * a
    print(f'A área de um tereno {l} x {a}')
    print(f'É de {area} m²')


# Programa Principal
print(' Controle de Terrenos')
print('-' * 30)
l = (float(input('LRGURA (m): ')))
a = (float(input('COMPRIMENTO (m): ')))
area(l, a)
print(area)