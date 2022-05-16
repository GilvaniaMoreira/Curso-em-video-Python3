valores = list()
resposta = ' '
while True:
    v = (int(input('Digite um valor: ')))
    valores.append(v)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resposta == 'SN':
         resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('-=' * 40)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse = True)
print(f'Os valores em ordem decrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
