listanúm = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in listanúm:
        listanúm.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print('-=' * 40)
listanúm.sort()
print(f'Você digitou os valores {listanúm}')