núm = (int(input('Digite um número: ')), 
       int(input('Digite outro número: ')), 
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: '))) #tupla onde o usuario insere as variavel
print(f'Você digitou os valores{núm}') #mostra na tela os valores inseridos
print(f'O valor de 9 apareceu {núm.count(9)} vezes') #count para ver quantas vezes o numero aparece na tupla
if 3 in núm: #Se 3 está dentro de numero faça:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else: #se não
    print('O valor 3 não foi digitado em nenhuma posição')
print('O valores digitados foram ', end='')
for n in núm: # Para cada número dentro de núm
    if n % 2 == 0: # verifico se o resto da divisão de n por 2 é 0
        print(n, end=' ') 
