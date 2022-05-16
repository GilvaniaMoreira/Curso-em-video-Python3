valores = list()
for c in range(0, 5):
    r = (int(input('Digite um valor: ')))
    if c == 0 or r > valores[-1] :
        valores.append(r)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if r <= valores[pos]:
                valores.insert(pos, r)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')


print(valores)