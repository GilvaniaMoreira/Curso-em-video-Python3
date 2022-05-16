soma = 0 
cont = 0
for c in range(1, 501, 2):
    if  c % 3 == 0:
        cont += 1 # cont = cont + 1
        soma += c # soma = soma + c
print('A soma de todos os {} valores solicitados é {}' .format(cont, soma))
#print('A soma de todos os números impares e multiplos de 3 entre 1 e 500 é {}' .format(soma))