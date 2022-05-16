#Comentarios
#expr = str(input('Digite a expressão: '))
#if expr.count('(') == expr.count(')'):
    #print('Sua expressão é válida!!')
#else:
    #print('Sua expressão não é válida')

#Explicação do Granabara
expr = str(input('Digite a expresão: ')) #começa o programa lendo a expressão 
pilha = [] # pilha é uma lista vazia
for símb in expr: # pra cada simbolo dentro da expressão:
    if símb == '(': # Se simbolo é igual '('
        pilha.append('(') #lista pilha inclui '(' 
    elif símb == ')': # Se simbolo é igual ')'
        if len(pilha) > 0: # Se o tamanho da minha lista for maior do que 0 é sinal de que ela não está vazia
            pilha.pop()# Remove o ultimo elemento da lista
        else: # Se não se a pilha estiver vazia:
            pilha.append(')') #incluir ')' um sinal que teve mais parentese '(' do que ')'
            break
if len(pilha) == 0: # Se o tamanho da lista for igual a 0: verifica se ainda resta parenteses na expressão
    print('Sua expressão está válida!')
else: # Se ainda tiver parenteses
    print('Sua expressão esta errada!')
