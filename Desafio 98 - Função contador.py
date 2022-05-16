from time import sleep


def contador(i, f, p):
    if p < 0:
        p+= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = 1
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -=p
        print('Fim!')
  
 

# Programa Principal
contador(0, 10, 1)
contador(10, 0, 2)
ini = (int(input('Inicio: ')))
fi = (int(input('Fim: ')))
pa = (int(input('Passo: ')))
contador(ini, fi, pa)

