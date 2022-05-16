p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
#Verificando quem é menor
menor = p 
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
print('O menor valor digitado foi {}' .format(menor))
#Verificando quem é o maior
maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t 
print('O maior valor digitad foi {}' .format(maior))