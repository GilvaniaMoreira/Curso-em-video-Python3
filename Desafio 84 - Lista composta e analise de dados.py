temp = list()
principal = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(principal)} pessoas.') # Exibir o tamanho da 
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='') #[] dentro da formatação é para delimitar e como mostrar não aparecer tudo junto
print() #print vazio, pula a linha, é o comando de saida do end=''
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')


