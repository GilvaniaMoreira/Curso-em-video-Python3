print('=' * 30)
print('{:^30}' .format('BANCO PABLO VITTAR'))
print('=' * 30)
valor = int(input('Que valor você quer sacar: R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd: #Se o total for maior ou igual a cedula faça:
        total -= céd #Entregando cedulas para fechar o valor solicitado pelo usuario.
        totcéd += 1 #contando quantas vezes se repete o loop para informar quantas cédulas serão necessarias
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO PABLO VITTAR! Tenha um bom dia!')