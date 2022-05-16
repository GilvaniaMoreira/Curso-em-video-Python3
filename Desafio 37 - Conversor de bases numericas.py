num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}' .format(num, bin(num)[2:])) #[2:] Fatiamento de string [posição incial : posição final] que vai ser mostrada para o usuario
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertendo para HEXADECIMAL é igual a {}' .format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente')
