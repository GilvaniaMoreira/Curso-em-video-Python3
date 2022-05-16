n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}' .format(n1, n2, media))
if media >= 5 and media < 7: # (7 > MEDIA >= 5) TAMBÉM PODE SE ESCREVER ASSIM, PRA NÃO USAR O AND.
    print('O aluno está RECUPERAÇÃO')
elif media < 5:
    print('O aluno está de REPROVADO')
else: #elif media >= 7
    print('O aluno está APROVADO')
