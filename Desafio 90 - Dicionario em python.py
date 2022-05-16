aluno = {}   #dicionario
aluno['nome'] = str(input('Nome do aluno: ')) #Dicionario recebe o chave nome com o que o usuario inserir
aluno['media'] = float(input(f'Média de {aluno["nome"]}: ')) #Dicionario recebe o chave média com o que o usuario inserir
if aluno["media"] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items(): 
    print(f'{k} é igual a {v}')

