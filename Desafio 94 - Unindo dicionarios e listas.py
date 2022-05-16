galera = list()
pessoas = dict()
soma = média = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera) # média calculada pelo total das idades e dividido pelo numero de pessoas cadastradas
print(f'A média de idade é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('<< ENCERRADO >>')
