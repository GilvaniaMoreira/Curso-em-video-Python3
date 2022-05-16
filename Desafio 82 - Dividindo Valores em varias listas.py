num = list()
resposta = ' '
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar [S/N] ')).strip().upper()
    if resposta in 'N':
        break
for i, v in enumerate:
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)    
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')