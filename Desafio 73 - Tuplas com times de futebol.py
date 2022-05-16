times =('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 
        'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
        'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense',
        'Sport', 'Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atlético-GO')
print('-=' *30)
print(f'Lista de times do Brasileirão {times}')
print('-=' *30)
print(f'Os primeiros 5 colocados são {times[0:5]}') #mostar os 5 ultimos
print('-=' *30)
print(f'Os 4 últimos são {times[-4:]}') #mostrar os 4 ultimos 
print('-=' *30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' *30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição') #times.index() procura qual posição a str está na tupla
