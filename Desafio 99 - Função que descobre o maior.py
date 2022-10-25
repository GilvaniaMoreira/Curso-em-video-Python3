from time import sleep

def maior(*num):
     print('Analisando os valores passados....')
     sleep(0.5)
     print(f'{num} ', end=' ')
     sleep(0.5)
     print(f'\nForam informdos {len(num)} valores ao todo.')
     print(f'O maior valor informado foi de {max(num)}')
     print('-=' * 30)
     


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)