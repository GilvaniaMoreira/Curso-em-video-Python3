listanum = list()
mai = menor = 0
for c in range(0, 5): # repetir 5 vezes
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0: 
        mai = men = listanum[c] #maior e menor recebe a posição do contador na lista
    else:
        if listanum[c] > mai: #Se o valor da lista digitado for maior que o maior 
            mai = listanum[c] #maior recebe valores na posição cont 
        if listanum[c] < men:# Se o valor da lista digitado for menor que o menor
            men = listanum[c] # menor recebe a lista valores na posição cont
print('=-' * 40)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum): # i = indice , v = valor , numerar da lista valores
    if v == mai: # Se valor for maior 
        print(f'{i}...', end='') # end='' continuar na mesma linha
print() #para pular de linha
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()

