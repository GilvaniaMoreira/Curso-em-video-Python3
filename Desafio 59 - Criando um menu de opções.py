from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('>>>>Qual a sua escolha?'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} total é {}' .format(n1, n2, soma))
    elif opcao == 2:
        multiplicação = n1 * n2
        print('A multiplicação de {} x {} total é {}' .format(n1, n2, multiplicação))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print('Entre {} e {} o maior número é {}' .format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente!')
        print('=-=' * 10)
    sleep(2)
print('Finalidado. Volte sempre!')