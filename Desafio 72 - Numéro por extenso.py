cont = ('zero','UM', 'Dois', 'Três', 'Quatro', 
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte') #Tupla 
while True: #loop infinito
    num = int(input('Digite um número entre 0 e 20: ')) #variavel que o usuario inseri
    if 0 <= num <= 20: # Se número for maior ou igual a zero e menor ou igual a vinte
        break #parar
    print('Tente novamente. ', end='') # mostar na tela novamente, se for incorreta a informação do usuario.
print(f'Você digitou o número {cont[num]}') # Mostar na tela a posição de uma variavel dentro da tupla.
