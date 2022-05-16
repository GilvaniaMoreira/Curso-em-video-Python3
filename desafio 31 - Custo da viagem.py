distancia = float(input('Qual a distãncia da viagem? '))
passagem = distancia * 0.5
passagemd = distancia * 0.45
if distancia >= 200:
    print('Você está preste a começar uma viagem de {}km' .format(distancia))
    print('e o preço da sua passagem será de RS{}'.format(passagemd))
else:
    print('Você está preste a começar uma viagem de {}km' .format(distancia))
    print('e o preço da sua passagem será de R${}'.format(passagem))
