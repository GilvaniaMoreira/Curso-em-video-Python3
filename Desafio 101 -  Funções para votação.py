def voto(ano):
    """
    Para economizar memoria, importamos dentro da função, pois só será importado na chamada da função
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.' 

# Programa Principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))