largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
metragem = (largura*altura)
tinta = metragem / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².' .format(largura, altura, metragem))
print('Para pintar a sua parede, você precisará de {}l de tinta.' .format(tinta))