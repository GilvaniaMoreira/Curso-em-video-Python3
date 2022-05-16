from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) # randomizado 5 numéros e estão dentro de uma tupla
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}') #'\n' no começo do print pula pra proxima linha
print(f'O menor valor sorteado foi {min(numeros)}')