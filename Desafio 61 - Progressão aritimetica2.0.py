print('Gerador de PA')
print('-=' *10)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = pt
contador = 1
while contador <= 10:
    print('{} ↠ ' .format(termo), end = '')
    termo += razao
    contador += 1
print('FIM')
