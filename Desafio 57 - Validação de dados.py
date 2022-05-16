sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
    print('Resposta incorreta tente novamente')
print('Sexo {} registrado com sucesso' .format(sexo))