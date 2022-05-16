print('='*10, 'GIL LOJAS', '='*10 )
preço = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3x ou mais no cartão''')
opção = float(input('Qual a sua opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2 
    print('Sua compra será parcelada em 2X de R$ {} SEM JUROS' . format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de RS{:.2f} COM JUROS' .format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. TENTE NOVAMENTE!')
print('Sua compra de R${} vai custar R${:.2f} no final.' .format(preço, total))
#if opção == 1:
    #total = preço - (preço * 10 / 100)
    #print('Sua compra de R${:.2f} vai custar R$ {:.2f} no final.' .format(preço, total))
#elif opção == 2:
    #total = preço - (preço * 5 / 100)
    #print('Sua compra de R${:.2f} vai custar R${:.2f} no final SEM JUROS.' .format(preço, total))
#elif opção == 3:
    #parcela = preço / 2
    #print('Sua compra será parcelada em 2x de R${:.2f}' .format(parcela))
#elif opção == 4:
    #parcela = int(input('Quantas parcelas? '))
    #vtotal = preço + (preço * 20 / 100)
    #vpar = vtotal / parcela
    #print('Sua compra será parcelada em {}x de R${} COM JUROS' .format(parcela, vpar ))
    #print('Sua compra de R${} vai custar {} no final.' .format(preço, vtotal))

