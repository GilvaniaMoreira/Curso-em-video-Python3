soma = 0
cont = 0
for c in range(1, 7): #Contando de 1 até 6 o ultimo numero ele não considera
    n = int(input('Digite o {} valor: ' .format(c)))
    if n % 2 ==0: # Se o resto da divisão de n por 2 for igual a zero 
        soma += n # soma = soma + n
        cont += 1 #cont = cont + 1
print('Você informou {} números e a soma dos valores digitados é {}' .format(cont, soma))