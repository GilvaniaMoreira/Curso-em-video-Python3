velocidade = float(input('Qual a velocidade do seu carro?'))
permitido = 80
multa = (velocidade-permitido) * 7
if velocidade > permitido:
    print('Multado! você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia! Diriga com segurança')
