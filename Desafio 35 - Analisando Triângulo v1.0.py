print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro seguemento: '))
r2 = float(input('Segundo seguemento: '))
r3 = float(input('Terceiro seguemento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!') 
