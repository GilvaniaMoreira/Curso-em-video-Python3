while True:
    n = int(input('Quer ver tabuada de qual valor? [Digite um número negativo para sair] '))
    if n < 0:
        break
    print('-' * 40)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. volte sempre!')

