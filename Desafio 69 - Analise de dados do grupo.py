tot18 = 0 # Variavél para o núemro de pessoas com 18 ou mais de idade
toth = 0 # Variavél para o núemro homens cadastrado
totf20 = 0 # Variavél para o núemro de mulheres com menos de 20 anos
while True: # Loop infinito só da pra sair com o comando break
    print('-' * 30)
    print('CADASTRE UMA PESSOA.')
    print('-' * 30)
    idade = int(input('Idade: ')) # A variavel idade recebe numeros inteiros que o usuario inserir
    sexo = ' '  # varival sexo inicia com str vazia (um espaço)
    while sexo not in 'MF': # Equanto na variavel não foi digitado M ou F faça:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0] #variavel recebe str(palavras) que o usuario inserir, tirando os espaços, colocando pra maiuscula e só pegando a primeira letra digitada
    if idade >= 18: # Se a idade for maior ou igual a 18 anos faça:
        tot18 += 1 # tot18 = tot18 + 1
    if sexo == 'M':
        toth +=1
    if sexo == 'F' and idade < 20:
        totf20 += 1  #totm18 = totm18 + 1
    print('-' * 30)
    resposta = ' '  # Variavel resposta inicia com str vazia (um espaço)
    while resposta not in 'SN': #Enquanto a resposta não for S ou N faça:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #variavel recebe str(palavras) que o usuario inserir, tirando os espaços, colocando pra maiuscula e só pegando a primeira letra digitada
    if resposta == 'N':  #Se a resposta for igual a N faça:
        break   # para sair da função while(enquanto)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totf20} mulheres com menos de 20 anos')