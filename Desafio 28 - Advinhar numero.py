from random import randint
from time import sleep
pc = randint(0, 5) # Faz o computador  "pensar" 
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == pc:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}' .format(pc, jogador))
