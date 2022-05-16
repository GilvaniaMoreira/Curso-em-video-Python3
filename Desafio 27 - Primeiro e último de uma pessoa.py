n = str(input('Digite seu nome completo: ')).strip() #strip = tirar os espacos antes e depois, entre as palavras não
nome = n.split()  #split = pegar o nome e fatiar em pedaços por espaço e cria uma lista.
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}' .format(nome[0]))
print('Seu último nome é {}' .format(nome[len(nome)-1])) #len = conta as posições do texto na lista