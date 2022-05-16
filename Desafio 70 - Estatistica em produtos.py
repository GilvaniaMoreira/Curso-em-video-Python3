totc = 0 #total do valor da compra
totmil = 0 #total de produtos custando mais de mil reais
menor = 0 # valor menor dos produtos comprados
baratop = ' ' # Nome do produto de menor valor
cont = 0 #contador
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço R$'))
    cont += 1
    totc += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor: # pra simplificar o codigo podemos só colocar o or preço < menor:
        menor = preço
        baratop = produto
    #else:
        #if preço < menor:
            #menor = preço
            #baratop = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
            break    
print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${totc:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {baratop} que custa {menor:.2f}')