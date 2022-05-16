print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro seguemento: '))
r2 = float(input('Segundo seguemento: '))
r3 = float(input('Terceiro seguemento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end='') #(end='') junta na mesma linha o proximo print
    if r1 == r2 == r3:
        print(' EQUILATERO!')
    elif r1 != r2 != r3 != r1: # Diferente (!=)
        print(' ESCALENO!')
    else :
        print(' ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!') 
