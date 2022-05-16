listagem = ('Lápis', '1.75', 
            'Borracha', '2',
            'Caderno', '15.90',
            'Estojo', '25',
            'Tranferidor', '4.20',
            'Compasso', '9.99',
            'Mochila', '120.32',
            'Canetas', '22.30',
            'Livro', '34.90')
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for posição in range(0, len(listagem)): #para cada posição em range'contagem' (vá de 0 ao comprimento de (tupla))
    if posição % 2 == 0: #Se o resto da divisão de posição por 2 for 2:
        print(f'{listagem[posição]:.<30}', end='') #Escreva posição da listagem formatado em 30 caracteres com ponto alinhado a esquerda 
    else:
        print(f'R$ {listagem[posição]:>7}')
#for item in listagem: #para cada itém dentro da tupla listagem:
#print(item, end='-')