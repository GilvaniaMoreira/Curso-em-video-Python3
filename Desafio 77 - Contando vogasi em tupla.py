palavra = ('aprender', 'progamar', 'linguagem','python'
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='') #\n esse comando quebra a linha
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')

