from datetime import date
atual = date.today().year # data atual do computador
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}' .format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATEMENTE!')
elif idade < 18:
    falta = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento' .format(falta))
elif idade > 18:
    passou = idade - 18
    print('Você já deveria ter se alistado a {} anos' .format(passou))
