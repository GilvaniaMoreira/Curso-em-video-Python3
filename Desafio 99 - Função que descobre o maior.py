from time import sleep

def maior(*num):
     print('Analisando os valores passados....')
     for c in range(1, len(num)):
          sleep(0.5)
          print(f'{num}', end=' ')
          #print(f'Foram informdos {len(num)} valores ao todo.')
     #print(f'O maior valor informado foi de {max(num)}')
     #print('-=' * 30)
     


maior(2, 9, 4, 5, 7, 1)
