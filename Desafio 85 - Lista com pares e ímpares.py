listan = list()
for c in range(1, 8):
    listan.append(int(input(f'Digite o {c}º valor: ')))
print('Os valores pares digitados foram: ', end='')
for n in listan:
    if n % 2 == 0:
        print(f'{n}', end=', ')
print()
print('Os valores ímpares digitados foram: ', end='')
for n in listan:
    if n % 2 == 1:
        print(f'{n}', end=', ' )