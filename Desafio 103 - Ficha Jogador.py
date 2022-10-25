def jogador(nome="<Desconhecido>", gol=0):
    print(f'O Jogador {nome} fez {gol} gols(s) no campeonato.')


# Programa Principal
print('-' * 30)
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(gol=g)
else:
    jogador(n, g)
