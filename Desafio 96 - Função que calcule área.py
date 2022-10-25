# Função para mostrar o titulo do programa
def titulo(msg):
    print('=' * len(msg))
    print(msg)
    print('=' * len(msg))    

# Função que calcula a área
def area(l, a):
    area = l * a
    print(f'A área de um tereno \n{l} x {a}')
    print(f'É de: {area} m²')


# Programa Principal
titulo('Controle de Terrenos')
l = (float(input('LRGURA (m): ')))
a = (float(input('COMPRIMENTO (m): ')))
area(l, a)
print(area)