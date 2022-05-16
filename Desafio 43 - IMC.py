peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}' .format(imc))
if imc < 15.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobre peso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')