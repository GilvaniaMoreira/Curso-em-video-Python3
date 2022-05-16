valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
tempo = int(input('Em quantos anos você quer pagar? '))
prestaçao = valor / (tempo * 12)
minino = salario *30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos' .format(valor, tempo), end='')
print(' a prestação será de R${:.2f}' .format(prestaçao), end='')
if prestaçao <= minino:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')